import os
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import fetch_california_housing

# Load California Housing dataset
housing = fetch_california_housing(as_frame=True)

# Features + target as a single DataFrame
df = housing.frame

# Quick check
print(df.head())
print(df.shape)

# Ensure the figs folder exists
os.makedirs("figs", exist_ok=True)

# Create and save the boxplot
plt.figure(figsize=(8, 6))
df.boxplot(column=["MedHouseVal"])
plt.title("Boxplot of Median House Value")
plt.ylabel("Value ($100k)")

# Save figure to figs/boxplot.png
plt.savefig("figs/boxplot.png")
plt.close()