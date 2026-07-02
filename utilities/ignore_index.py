import pandas as pd

# Load the CSV
path = '/home/huzaifa/Code/TensorCodeProblemSet/Benin_NOAI/X_testset.csv'
df = pd.read_csv(path)

# Remove the 'id' column if it exists
df = df.drop(columns=["id",'Unnamed: 0'], errors="ignore")

# Reset the DataFrame index
df = df.reset_index(drop=True)

# Save without writing the index to the CSV
df.to_csv(path, index=False)

print(df.head(1))