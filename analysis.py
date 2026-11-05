# US Honey Dataset - Visualisation Practice
# Dataset: US_honey_dataset.csv

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# Importing data
df = pd.read_csv("data/US_honey_dataset.csv")

# Basic dataset inspection
df.info()
print(df.describe())
print(f"Shape of the DataFrame: {df.shape}")
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# 1. Which state has produced the highest amount of honey throughout all available years?
High_prof_state = (
    df.groupby("state")["production"]
      .sum()
      .sort_values(ascending=False)
      .reset_index()
)

plt.figure(figsize=(12, 8))
sns.barplot(data=High_prof_state, x="production", y="state",
            hue="state", palette="coolwarm", legend=False)
plt.title("Honey Production by State")
plt.xlabel("Production")
plt.ylabel("State")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# 2. Which state has the highest and lowest yield per colony throughout all years?
yield_per_col = (
    df.groupby("state")["yield_per_colony"]
      .mean()
      .sort_values(ascending=False)
      .reset_index()
)
print(yield_per_col.head())

plt.figure(figsize=(12, 8))
sns.barplot(data=yield_per_col, x="yield_per_colony", y="state",
            hue="state", palette="summer", legend=False)
plt.title("Average Yield/Colony by State")
plt.xlabel("Average yield per colony")
plt.ylabel("State")
plt.tight_layout()
plt.show()

# 3. Which state has the highest and lowest number of colonies?
grouped_col = (
    df.groupby("state")["colonies_number"]
      .sum()
      .sort_values(ascending=False)
      .reset_index()
)

plt.figure(figsize=(12, 8))
sns.barplot(data=grouped_col, x="colonies_number", y="state",
            hue="state", palette="summer", legend=False)
plt.title("Total Number of Colonies by State")
plt.xlabel("Number of Colonies")
plt.ylabel("State")
plt.grid(alpha=0.4)
plt.tight_layout()
plt.show()

# 4. Which state had the highest honey stock in 2020?
df_2020 = df[df["year"] == 2020]
Gd = (
    df_2020.groupby("state")["stocks"]
           .sum()
           .sort_values(ascending=False)
           .reset_index()
)

plt.figure(figsize=(12, 8))
sns.barplot(data=Gd, x="state", y="stocks",
            hue="state", palette="summer", legend=False)
plt.title("Stock by State in 2020 Year")
plt.xlabel("State")
plt.ylabel("Stocks")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# 5. Correlation between numerical columns
corr = df.corr(numeric_only=True)
plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Heatmap")
plt.tight_layout()
plt.show()
