import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader, random_split

# ============================================================
# Device Agnostic Code
# ============================================================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

# ============================================================
# Load Data
# ============================================================
train_df = pd.read_csv("/home/huzaifa/Code/TensorCodeProblemSet/MNIST_classifier/Training_Set.csv")
test_df = pd.read_csv("/home/huzaifa/Code/TensorCodeProblemSet/MNIST_classifier/X_testset.csv")

# ============================================================
# Check Class Distribution (Imbalance Check)
# ============================================================
print("\nClass Distribution:")
print(train_df["target"].value_counts().sort_index())

# ============================================================
# Dataset Class
# ============================================================
class MNISTDataset(Dataset):
    def __init__(self, df, is_train=True):
        self.is_train = is_train
        if is_train:
            self.X = df.drop(columns=["target"]).values.astype(np.float32) / 255.0
        else:
            self.X = df.values.astype(np.float32) / 255.0
        if is_train:
            self.y = df["target"].values.astype(np.int64)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        x = torch.tensor(self.X[idx])
        if self.is_train:
            y = torch.tensor(self.y[idx])
            return x, y
        return x

# ============================================================
# Train/Validation Split
# ============================================================
dataset = MNISTDataset(train_df, is_train=True)

train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size

train_data, val_data = random_split(dataset, [train_size, val_size])

train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
val_loader = DataLoader(val_data, batch_size=64, shuffle=False)

# ============================================================
# Model 
# ============================================================
class MNISTModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(784, 512),
            nn.GELU(),
            nn.Linear(512, 256),
            nn.GELU(),
            nn.Linear(256, 128),
            nn.GELU(),
            nn.Linear(128, 10),
            
        )

    def forward(self, x):
        return self.net(x)

model = MNISTModel().to(device)

# ============================================================
# Loss and Optimizer
# ============================================================
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# ============================================================
# Training Loop
# ============================================================
epochs = 20

for epoch in range(epochs):
    model.train()
    train_loss = 0

    for x, y in train_loader:
        x, y = x.to(device), y.to(device)

        optimizer.zero_grad()
        outputs = model(x)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()

        train_loss += loss.item()

    # ========================================================
    # Validation
    # ========================================================
    model.eval()
    correct = 0
    total = 0
    val_loss = 0

    with torch.inference_mode():
        for x, y in val_loader:
            x, y = x.to(device), y.to(device)
            outputs = model(x)
            loss = criterion(outputs, y)
            val_loss += loss.item()

            preds = torch.argmax(outputs, dim=1)
            correct += (preds == y).sum().item()
            total += y.size(0)

    acc = correct / total

    print(f"Epoch {epoch+1}")
    print(f"Train Loss: {train_loss:.4f} | Val Loss: {val_loss:.4f} | Val Acc: {acc:.4f}")
    print("-" * 50)

# ============================================================
# Prediction on Test Set
# ============================================================
test_dataset = MNISTDataset(test_df, is_train=False)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

model.eval()
predictions = []

with torch.no_grad():
    for x in test_loader:
        x = x.to(device)
        outputs = model(x)
        preds = torch.argmax(outputs, dim=1)
        predictions.extend(preds.cpu().numpy())

# ============================================================
# Save Submission
# ============================================================
submission = pd.DataFrame({
    "target": predictions
})

submission.to_csv("submission.csv", index=False)

print("Submission saved as submission.csv")