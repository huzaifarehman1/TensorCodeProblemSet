import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from torchmetrics import Precision
import seaborn as sns
import matplotlib.pyplot as plt
# -------------------------
# Load Data
# -------------------------
train_path = ''
test_path = ''


train = pd.read_csv(train_path)
test = pd.read_csv(test_path)

sns.scatterplot(train,x='x_loc',y = 'y_loc',hue='target')
plt.show()



X_train = train[["x_loc", "y_loc"]].values
y_train = train["target"].values.reshape(-1, 1)

X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32)
X_test = torch.tensor(test[["x_loc", "y_loc"]].values,
                      dtype=torch.float32)

train_loader = DataLoader(
    TensorDataset(X_train, y_train),
    batch_size=len(X_train),
    shuffle=True
)

# -------------------------
# Neural Network
# -------------------------
class Net(nn.Module):
    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(2, 8),
            nn.Tanh(),

            nn.Linear(8, 8),
            nn.Tanh(),
            nn.Linear(8,1),
            nn.Sigmoid()
           
        )

    def forward(self, x):
       
        x_loc = x[:, 0:1]
        y_loc = x[:, 1:2]

        # Feature engineering inside the network
        r2 = x_loc.pow(2) + y_loc.pow(2)
        theta = torch.atan2(y_loc, x_loc)
        
        r2 = (r2-r2.mean())/r2.std()
        theta = (theta-theta.mean())/theta.std()
        
        features = torch.cat([r2, theta], dim=1)

        return self.network(features)
        
model = Net()

# -------------------------
# Training
# -------------------------
criterion = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
Metric = Precision('binary')

epochs = 100

for epoch in range(epochs):

    model.train()
    epoch_loss = 0

    for xb, yb in train_loader:

        optimizer.zero_grad()

        pred = model(xb)
        loss = criterion(pred, yb)

        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()
        
        if (0) % 10 == 0:
            print(
                f"Epoch {epoch+1:3d} "
                f"Loss: {epoch_loss/len(train_loader):.4f}"
            )
            print(f'metric = {Metric(pred,yb)}')


# -------------------------
# Prediction
# -------------------------

model.eval()

with torch.inference_mode():
    probs = model(X_test)
   


submission = pd.DataFrame({
    "target": (probs[:,0] > 0.5).long()
})

submission.to_csv("submission.csv", index=False)
print("\nSaved submission.csv")