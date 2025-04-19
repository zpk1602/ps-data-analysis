import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Create charts folder for our charts
os.makedirs("charts", exist_ok=True)

# Load the CSV file that we downloaded from Kaggle
df = pd.read_csv("vgsales.csv")

# We need to filter for PlayStation platforms
playstation_platforms = ["PS", "PS2", "PS3", "PS4", "PS5", "PSP", "PSV"]
df_ps = df[df["Platform"].isin(playstation_platforms)]

# Clean up wherever we have missing year values, and convert year to int
df_ps = df_ps.dropna(subset=["Year"])
df_ps["Year"] = df_ps["Year"].astype(int)

# Count PlayStation game releases per year
# Stored as a series
releases_per_year = df_ps["Year"].value_counts().sort_index()

# Plot the bar chart of our dataframe
plt.figure(figsize=(10, 5))
sns.barplot(x=releases_per_year.index, y=releases_per_year.values, color="skyblue")
plt.title("PlayStation Games Released Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Games")
# Rotating the X label makes them easier to read
plt.xticks(rotation=45)
# Fixes spacing/cutoffs
plt.tight_layout()
plt.savefig("charts/releases_per_year.png")
plt.close()

print("Chart saved to: charts/releases_per_year.png")
