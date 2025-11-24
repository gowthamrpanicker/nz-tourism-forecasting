import pandas as pd

file_list = ["datasets/csv datasets/international-travel/NZ-resident traveller arrivals by main destination, purpose, age and sex (Monthly)-2024-1.csv", "datasets/csv datasets/international-travel/NZ-resident traveller arrivals by main destination, purpose, age and sex (Monthly)-2024-2.csv", "datasets/csv datasets/international-travel/NZ-resident traveller arrivals by main destination, purpose, age and sex (Monthly)-2025.csv"]
output_file="datasets/csv datasets/international-travel/NZ-resident traveller arrivals by main destination, purpose, age and sex (Monthly).csv"
date_col="Date"

# Read and concatenate all files
df = pd.concat([pd.read_csv(f) for f in file_list], ignore_index=True)

# Ensure Date is in datetime format
df[date_col] = pd.to_datetime(df[date_col], dayfirst=True, errors='coerce')

# Sort by date
df = df.sort_values(by=date_col).reset_index(drop=True)

# Save to output file if provided
if output_file:
    df.to_csv(output_file, index=False)
    print(f"✅ Combined CSV saved to: {output_file}")