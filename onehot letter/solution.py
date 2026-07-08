# You need Pytorch for this!
import torch
import torch.nn as nn
import pandas as pd
import torch.nn.functional as F


# -----------------------------
# Model Architecture
# -----------------------------
torch.manual_seed(35)
class SimpleNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()

        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x


model = SimpleNet(
    input_size=26,
    hidden_size=128,
    output_size=50
)



train_path = ''



# -----------------------------
# Create letter fingerprints
# -----------------------------

with torch.no_grad():

    fingerprints = []

    for i in range(26):

        x = torch.zeros(1,26)

        # one-hot letter
        x[0,i] = 1

        output = model(x)

        fingerprints.append(
            output.squeeze(0)
        )


fingerprints = torch.stack(fingerprints)


# -----------------------------
# Load test vectors
# -----------------------------

test = pd.read_csv(train_path)

X_test = torch.tensor(
    test.values,
    dtype=torch.float32
)


# -----------------------------
# Compare using cosine similarity
# -----------------------------

def cosine_similarity(a,b):

    return F.cosine_similarity(
        a.unsqueeze(0),
        b.unsqueeze(0)
    )


predictions = []


for sample in X_test:

    best_score = -999
    best_letter = -1

    for letter in range(26):

        score = cosine_similarity(
            sample,
            fingerprints[letter]
        ).item()


        if score > best_score:
            best_score = score
            best_letter = letter + 1


    predictions.append(best_letter)



# -----------------------------
# Create submission
# -----------------------------

submission = pd.DataFrame({
    "target": predictions
})


submission.to_csv(
    "submission.csv",
    index=False
)


print(submission.head())