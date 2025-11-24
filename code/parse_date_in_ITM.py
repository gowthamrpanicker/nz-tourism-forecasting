import pandas as pd
from pandas.tseries.offsets import MonthEnd

def convert_travel_dates(in_csv: str, out_csv: str) -> None:
    """
    Convert 'Month' column from 'YYYYMmm' (e.g., 1998M01) to
    'YYYY-MM-DD' where the day is the last day of that month.
    """
    df = pd.read_csv(in_csv)

    # Parse format like 1998M01 → datetime (1998-01-01)
    df["Month"] = pd.to_datetime(df["Month"], format="%YM%m", errors="coerce")

    # Shift to month-end
    df["Month"] = (df["Month"] + MonthEnd(0)).dt.strftime("%Y-%m-%d")

    df.to_csv(out_csv, index=False)
    print(f"✅ Converted and saved -> {out_csv}")

if __name__ == "__main__":
    convert_travel_dates("datasets\Visitor arrival totals (Monthly).csv", "datasets\Visitor arrival totals (Monthly)_changed.csv")
