from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw/startup_investments.csv")

def load_raw_csv(path: Path = RAW_PATH) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Raw file not found: {path}")

    # Robust encoding handling for Kaggle/Windows exports
    encodings = ["utf-8", "utf-8-sig", "cp1252", "latin1"]
    last_err = None
    for enc in encodings:
        try:
            df = pd.read_csv(path, encoding=enc, low_memory=False)
            return df
        except Exception as e:
            last_err = e
    raise last_err
