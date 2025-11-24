import pandas as pd
import os
import numpy as np

input_path = "datasets/csv datasets/ADP_All_Measures_.csv"
output_path = "datasets/csv datasets/ADP_All_Measures.csv"

os.makedirs(os.path.dirname(output_path), exist_ok=True)

# read CSV
df = pd.read_csv(input_path)

# month to datetime
df["Month"] = pd.to_datetime(df["Month"], dayfirst=True, errors="coerce")

# Convert Value to numeric (force errors to NaN if any bad strings exist)
df["Value"] = pd.to_numeric(df["Value"], errors="coerce")
df["Value"] = df["Value"].replace("", np.nan)

df_wide = df.pivot_table(
    index=["Month", "Area type", "Area", "Property"],
    columns="Measure",
    values="Value",
    aggfunc="first"
).reset_index()

# Keep only necessary rows
df_wide = df_wide[df_wide["Property"] == "Total"].copy()

# Keep only necessary columns
cols_keep = [
    "Month",
    "Domestic guest nights",
    "International guest nights",
    "Total guest nights"
]
df_wide = df_wide[cols_keep]


df_wide.columns.name = None

df_wide = df_wide.dropna()

df_wide.to_csv(output_path, index=False)

print(f"Processed file saved to: {output_path}")
print(df_wide.head())
