import pandas as pd

# Read the two CSV files
df1 = pd.read_csv("datasets/cleaned_and_processed/international-visitor-survey-data-quarter-1-2025/survey_main_header_cleaned.csv")
df2 = pd.read_csv("datasets/csv datasets/international-visitor-survey-data-quarter-1-2025/visitor_satisfaction.csv")

# Join them on a common column (e.g., "id")
# You can change 'id' to the actual column name you want to join on
merged_df = pd.merge(df1, df2, on="response_id", how="inner")

# Save the result as a new CSV
merged_df.to_csv("datasets/cleaned_and_processed/visitor_survey.csv", index=False)

print("Merged CSV saved as visitor_survey.csv")
