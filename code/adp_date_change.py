import pandas as pd
from pandas.tseries.offsets import MonthEnd

def convert_adp_dates(in_csv: str, out_csv: str) -> None:
    """
    Converts 'Month' from YYYY-DD-MM (e.g., 2020-01-06 meaning 2020-06-01)
    to proper YYYY-MM-DD at month-end (e.g., 2020-06-30).
    Writes the cleaned file to out_csv with 'Month' as month-end.
    """
    df = pd.read_csv(in_csv)

    # Parse the odd format and normalize to month-end
    month_parsed = pd.to_datetime(df["Month"].astype(str).str.strip(),
                                  format="%Y-%d-%m", errors="coerce")
    month_end = month_parsed + MonthEnd(0)

    df["Month"] = month_end.dt.strftime("%Y-%m-%d")

    df.to_csv(out_csv, index=False)

if __name__ == "__main__":
    convert_adp_dates("datasets\ADP_All_Measures.csv", "datasets\ADP_All_Measures_changed.csv")
    print(f"Converted and saved")
