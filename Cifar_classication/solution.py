import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader,random_split

class CIFARCSV(Dataset):
    def __init__(self, csv_file,Train = True):
        df = pd.read_csv(csv_file)
        if Train:
            self.X = df.drop(columns=["target"]).values.astype(np.float32)
            self.y = df["target"].values.astype(np.int64)
        else:    
            self.X = df.values.astype(np.float32)
        # normalize pixels (0–255 → 0–1)
        self.X = self.X / 255.0
        self.train = Train
    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        x = self.X[idx]
        y = torch.tensor([0])
        if self.train:
            y = self.y[idx]
            y = torch.tensor(y)

        # reshape 3072 → (3, 32, 32)
        x = torch.tensor(x).view(3, 32, 32)
        
        return x, y

path_train = ''
path_test = ''

train_dataset = CIFARCSV(path_train,True)
train,val = random_split(train_dataset,[0.90,0.10])

test_dataset = CIFARCSV(path_test,False)

train_loader = DataLoader(train, batch_size=16, shuffle=True)
val_loader = DataLoader(val,batch_size=16)
test_loader = DataLoader(test_dataset, batch_size=16, shuffle=False)  


class CIFARNet(nn.Module):
    def __init__(self, num_classes=20):  # CIFAR-100 coarse = 20
        super().__init__()

        self.features = nn.Sequential(

            nn.Conv2d(3, 64, 3, padding=1),
            nn.BatchNorm2d(64),
            nn.GELU(),

            nn.Conv2d(64, 128, 3),
            nn.BatchNorm2d(128),
            nn.GELU(),

            nn.MaxPool2d(2),  

            nn.Conv2d(128, 256, 3),
            nn.BatchNorm2d(256),
            nn.GELU(),

            nn.MaxPool2d(2),  # 8x8

            nn.Conv2d(256, 512, 3),
            nn.BatchNorm2d(512),
            nn.GELU(),

            nn.AdaptiveAvgPool2d((1, 1))  
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(512, 256),
            nn.GELU(),
            nn.Linear(256, num_classes)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = CIFARNet(num_classes=20).to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.AdamW(model.parameters(), lr=0.001)

def train_one_epoch():
    model.train()
    total_loss = 0

    for x, y in train_loader:
        x, y = x.to(device), y.to(device)

        optimizer.zero_grad()
        logits = model(x)
        loss = criterion(logits, y)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    return total_loss / len(train_loader)


def evaluate():
    model.eval()
    correct = 0
    total = 0

    with torch.inference_mode():
        for x, y in val_loader:
            x, y = x.to(device), y.to(device)

            logits = model(x)
            preds = torch.argmax(logits, dim=1)

            correct += (preds == y).sum().item()
            total += y.size(0)

    return correct / total

EPOCHS = 10

for epoch in range(EPOCHS):
    loss = train_one_epoch()
    acc = evaluate()

    print(f"Epoch {epoch+1}/{EPOCHS} | Loss: {loss:.4f} | Acc: {acc:.4f}")
    
model.eval()

predictions = []

with torch.inference_mode():
    for x, _ in test_loader:   # Ignore the dummy target
        x = x.to(device)

        logits = model(x)
        preds = torch.argmax(logits, dim=1)

        predictions.extend(preds.cpu().numpy())


submission = pd.DataFrame({
    "target": predictions
})

submission.to_csv("submission.csv", index=False)

print("Prediction file saved!")
           