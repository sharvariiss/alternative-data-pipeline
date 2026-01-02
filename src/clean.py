import re
import pandas as pd

def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [re.sub(r"\s+", "_", c.strip().lower()) for c in df.columns]
    return df

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = standardize_columns(df)

    # Drop exact duplicates
    df = df.drop_duplicates()

    # Trim strings
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip()

    # Coerce some common numeric fields if present
    for num_col in ["funding_total_usd", "funding_rounds", "founded_year"]:
        if num_col in df.columns:
            df[num_col] = pd.to_numeric(df[num_col], errors="coerce")

    return df
