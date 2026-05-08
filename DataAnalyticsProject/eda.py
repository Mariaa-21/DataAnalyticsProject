import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
df = pd.read_csv("books.csv")

# Show first rows
print(df.head())

# Dataset information
print(df.info())

# Remove currency symbol safely
df["Price"] = df["Price"].replace(r"[^0-9.]", "", regex=True)

# Convert to float
df["Price"] = df["Price"].astype(float)

# Show statistics
print(df.describe())

# Plot graph
plt.figure(figsize=(10,5))

sns.histplot(df["Price"], bins=10)

plt.title("Book Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")

plt.show()