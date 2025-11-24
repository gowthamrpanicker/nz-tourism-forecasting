import pandas as pd
import glob
import os

# i/p & o/p paths
input_folder = "dataset/csv datasets/TECT"
output_folder = "dataset/csv datasets/TECT"


os.makedirs(output_folder, exist_ok=True)

# extensions
extensions = ["*.xlsx", "*.xls", "*.xlsb"]

for ext in extensions:
    for file in glob.glob(os.path.join(input_folder, ext)):
        filename = os.path.splitext(os.path.basename(file))[0]

        try:
            # Use correct engine based on file type
            if file.endswith(".xlsb"):
                df = pd.read_excel(file, sheet_name=1, engine="pyxlsb")
            else:
                df = pd.read_excel(file, sheet_name=1)
                
            # Fix Date column if present
            if "Date" in df.columns:
                col = df["Date"]

                # Case 1: Already datetime
                if pd.api.types.is_datetime64_any_dtype(col):
                    pass  # do nothing

                # Case 2: Numeric → Excel serial date
                elif pd.api.types.is_numeric_dtype(col):
                    df["Date"] = pd.to_datetime(col, origin="1899-12-30", unit="D", errors="coerce")

                # Case 3: Strings
                else:
                    df["Date"] = pd.to_datetime(col, errors="coerce", dayfirst=True)


            # Save to CSV
            output_file = os.path.join(output_folder, filename + ".csv")
            df.to_csv(output_file, index=False)
            print(f"Converted (2nd sheet): {file} → {output_file}")

        except Exception as e:
            print(f"❌ Failed to convert {file}: {e}")