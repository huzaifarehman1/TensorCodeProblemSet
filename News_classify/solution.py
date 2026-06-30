import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.normalizers import Lowercase, NFD
from tokenizers.normalizers import Sequence as NormalizerSequence
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.pre_tokenizers import Sequence as PreTokenizerSequence
from tokenizers.trainers import BpeTrainer
from tokenizers.processors import TemplateProcessing
import os

# ============================================================
# Configuration
# ============================================================

TRAIN_PATH = "/home/huzaifa/Code/TensorCodeProblemSet/News_classify/Training_Set.csv"
TEST_PATH = "/home/huzaifa/Code/TensorCodeProblemSet/News_classify/X_testset.csv"

TEXT_FILE = "text.txt"
TOKENIZER_PATH = "tokenizer.json"

VOCAB_SIZE = 30000
MAX_LEN = 300

BATCH_SIZE = 8
EMBED_DIM = 256
NHEAD = 8
NUM_LAYERS = 4

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ============================================================
# Train / Load Tokenizer
# ============================================================
if not os.path.exists(TEXT_FILE):

    train_df = pd.read_csv(TRAIN_PATH)

    with open(TEXT_FILE, "w", encoding="utf-8") as f:
        for text in train_df["Text"]:
            f.write(str(text).strip() + "\n")

    print("Created text.txt")

try:
    tokenizer = Tokenizer.from_file(TOKENIZER_PATH)
    print("Tokenizer loaded.")

except:
    print("Training tokenizer...")

    tokenizer = Tokenizer(BPE(unk_token="[UNK]"))

    tokenizer.normalizer = NormalizerSequence([
        NFD(),
        Lowercase()
    ])

    tokenizer.pre_tokenizer = PreTokenizerSequence([
        Whitespace()
    ])

    trainer = BpeTrainer(
        vocab_size=VOCAB_SIZE,
        min_frequency=5,
        special_tokens=[
            "[PAD]",
            "[SEP]",
            "[UNK]",
            "[CLS]"
        ]
    )

    tokenizer.train([TEXT_FILE], trainer)

    tokenizer.enable_padding(
        pad_id=tokenizer.token_to_id("[PAD]"),
        pad_token="[PAD]",
        length=MAX_LEN
    )

    tokenizer.enable_truncation(MAX_LEN)

    tokenizer.post_processor = TemplateProcessing(
        single="[CLS] $A [SEP]",
        special_tokens=[
            ("[CLS]", tokenizer.token_to_id("[CLS]")),
            ("[SEP]", tokenizer.token_to_id("[SEP]"))
        ]
    )

    tokenizer.save(TOKENIZER_PATH)

    print("Tokenizer saved.")

tokenizer = Tokenizer.from_file(TOKENIZER_PATH)

# ============================================================
# Dataset
# ============================================================

class NewsDataset(Dataset):

    def __init__(self, dataframe, train=True):

        self.text = []
        self.mask = []

        if train:
            self.labels = torch.tensor(
                dataframe["target"].values,
                dtype=torch.long
            )

        for sentence in dataframe["Text"]:

            encoding = tokenizer.encode(sentence)

            self.text.append(
                torch.tensor(encoding.ids, dtype=torch.long)
            )

            self.mask.append(
                torch.tensor(encoding.attention_mask, dtype=torch.bool)
            )

        self.train = train

    def __len__(self):
        return len(self.text)

    def __getitem__(self, idx):

        if self.train:
            return (
                self.text[idx],
                self.mask[idx]
            ), self.labels[idx]

        return self.text[idx], self.mask[idx]

# ============================================================
# Model
# ============================================================

class TransformerClassifier(nn.Module):

    def __init__(
        self,
        vocab_size=VOCAB_SIZE,
        embed_dim=EMBED_DIM,
        max_len=MAX_LEN,
        nhead=NHEAD,
        num_layers=NUM_LAYERS,
        classes=5
    ):

        super().__init__()

        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.position = nn.Embedding(max_len, embed_dim)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=embed_dim,
            nhead=nhead,
            dim_feedforward=embed_dim * 4,
            activation=torch.nn.functional.gelu,
            batch_first=True
        )

        self.encoder = nn.TransformerEncoder(
            encoder_layer,
            num_layers=num_layers
        )

        self.norm_Embedding = nn.LayerNorm(embed_dim)
        self.norm_finalOutput = nn.LayerNorm(embed_dim)

        self.classifier = nn.Linear(embed_dim, classes)

    def forward(self, ids, mask):

        batch, seq = ids.shape

        x = self.embedding(ids)

        positions = torch.arange(
            seq,
            device=ids.device
        ).expand(batch, -1)

        x = x + self.position(positions)

        x = self.norm_Embedding(x)

        # True means ignore the token.
        x = self.encoder(
            x,
            src_key_padding_mask=~mask
        )

        # CLS Token
        x = x[:, 0]

        x = self.norm_finalOutput(x)

        return self.classifier(x)

# ============================================================
# Load Data
# ============================================================

train_df = pd.read_csv(TRAIN_PATH)

num_classes = train_df["target"].nunique()

train_dataset = NewsDataset(train_df)

train_loader = DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)

# ============================================================
# Training
# ============================================================

model = TransformerClassifier(classes=num_classes).to(DEVICE)

criterion = nn.CrossEntropyLoss().to(DEVICE)

optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=0.0001
)

EPOCHS = 10

for epoch in range(EPOCHS):
    batch = 0
    model.train()

    total_loss = 0

    for (ids, mask), labels in train_loader:
        batch += 1
        ids = ids.to(DEVICE)
        mask = mask.to(DEVICE)
        labels = labels.to(DEVICE)

        predictions = model(ids, mask)

        loss = criterion(predictions, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
        if batch%10 == 0:
            print(
                f"Epoch {epoch+1}/{EPOCHS} | "
                f"Loss: {total_loss/batch:.4f}"
            )

# ============================================================
# Prediction
# ============================================================

test_df = pd.read_csv(TEST_PATH)

test_dataset = NewsDataset(test_df, train=False)

test_loader = DataLoader(
    test_dataset,
    batch_size=BATCH_SIZE
)

model.eval()

predictions = []

with torch.inference_mode():

    for ids, mask in test_loader:

        ids = ids.to(DEVICE)
        mask = mask.to(DEVICE)

        output = model(ids, mask)

        pred = output.argmax(dim=1)

        predictions.extend(pred.cpu().numpy())

submission = pd.DataFrame({
    "target": predictions
})

submission.to_csv("submission.csv", index=False)

print("Submission saved.")