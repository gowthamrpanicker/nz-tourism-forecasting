import pandas as pd
import os

input_path = "datasets/csv datasets/international-visitor-survey-data-quarter-1-2025/survey_main_header.csv"
output_path = "datasets/cleaned_and_processed/international-visitor-survey-data-quarter-1-2025/survey_main_header_cleaned.csv"

os.makedirs(os.path.dirname(output_path), exist_ok=True)

# load CSV
df = pd.read_csv(input_path)

# remove unwanted columns
cols_to_drop = [
    "no_days_in_nz_unknown",
    "no_selection_itinerary",
    "package_deal",
    "pkg_included_airfare",
    "country_package_started",
    "trip_start_country",
    "incl_stay_other_country",
    "no_nights_other_country",
    "single_or_others currency",
    "other_purchase"
]
df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])  # drop only if exists

# Replace NA with 0 in people count columns
for col in ["no_people_over_15", "no_people_under_15"]:
    if col in df.columns:
        df[col] = df[col].fillna(1).astype(int)  # force int for cleaner output

# save CSV
df.to_csv(output_path, index=False)

print(f"Cleaned dataset saved to: {output_path}")
print(df.head())
