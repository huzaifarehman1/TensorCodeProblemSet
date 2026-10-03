import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler


# ============================================================
# 1. LOAD DATA
# ============================================================

train = pd.read_csv("/home/huzaifa/Code/TensorCodeProblemSet/Unseen_ways/training.csv")

FEATURES = ["Feature_1", "Feature_2", "Feature_3", "Feature_4"]
TARGET = "class"

X = train[FEATURES].copy()
y = train[TARGET].copy()


# ============================================================
# 2. STANDARDIZE FEATURES
# ============================================================

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# ============================================================
# 3. APPLY t-SNE
# ============================================================

tsne = TSNE(
    n_components=2,
    perplexity=30,
    learning_rate="auto",
    random_state=42
)

X_tsne = tsne.fit_transform(X_scaled)

train["TSNE_1"] = X_tsne[:, 0]
train["TSNE_2"] = X_tsne[:, 1]


sns.scatterplot(x=train["TSNE_1"],y=train["TSNE_2"],hue = y)
plt.show()


lables = X_tsne[:,0] > 0
lables = np.asarray(lables,dtype=np.int16)
lables += 1


sns.scatterplot(x=train["TSNE_1"],y=train["TSNE_2"],hue = lables)
plt.show()


sns.scatterplot(x=train["TSNE_1"],y=train["TSNE_2"],hue = lables-y)
plt.show()



submission = pd.DataFrame({"target":lables})

submission.to_csv(
    "submission.csv",
    index=False
)

print(submission.head())

