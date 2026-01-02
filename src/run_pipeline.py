from pathlib import Path
import pandas as pd

from src.ingest import load_raw_csv
from src.clean import clean_dataframe
from src.validate import validate

OUT_CLEAN = Path("data/processed/clean.csv")
REPORT_MD = Path("reports/results.md")

def main():
    df_raw = load_raw_csv()
    raw_rows, raw_cols = df_raw.shape

    df_clean = clean_dataframe(df_raw)
    clean_rows, clean_cols = df_clean.shape

    validation = validate(df_clean)

    OUT_CLEAN.parent.mkdir(parents=True, exist_ok=True)
    df_clean.to_csv(OUT_CLEAN, index=False)

    REPORT_MD.parent.mkdir(parents=True, exist_ok=True)

    missing_summary = (df_clean.isna().mean().sort_values(ascending=False).head(10) * 100).round(2)

    with open(REPORT_MD, "w", encoding="utf-8") as f:
        f.write("# Alternative Data Pipeline Report\n\n")
        f.write("## Dataset Summary\n\n")
        f.write(f"- Raw shape: **{raw_rows} rows × {raw_cols} columns**\n")
        f.write(f"- Clean shape: **{clean_rows} rows × {clean_cols} columns**\n")
        f.write(f"- Output file: `{OUT_CLEAN.as_posix()}`\n\n")

        f.write("## Validation Results\n\n")
        f.write(f"**Pipeline status:** {'✅ PASSED' if validation['passed'] else '❌ FAILED'}\n\n")
        for c in validation["checks"]:
            status = "✅" if c["passed"] else "❌"
            detail = f" — {c['detail']}" if c["detail"] else ""
            f.write(f"- {status} {c['name']}{detail}\n")

        f.write("\n## Top Missing Columns (percent)\n\n")
        f.write(missing_summary.to_frame("missing_%").to_markdown() + "\n")

    print("[OK] Saved clean data:", OUT_CLEAN)
    print("[OK] Wrote report:", REPORT_MD)
    print("[OK] Validation passed:", validation["passed"])

if __name__ == "__main__":
    main()
