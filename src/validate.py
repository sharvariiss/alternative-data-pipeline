import pandas as pd

def validate(df: pd.DataFrame) -> dict:
    report = {"passed": True, "checks": []}

    def check(name: str, condition: bool, detail: str = ""):
        report["checks"].append({"name": name, "passed": bool(condition), "detail": detail})
        if not condition:
            report["passed"] = False

    # Basic checks
    check("non_empty_dataset", len(df) > 0, f"rows={len(df)}")

    # Column checks (common Crunchbase-like columns)
    required_any = ["name", "market", "category_list", "status"]
    present = [c for c in required_any if c in df.columns]
    check("has_any_key_columns", len(present) >= 2, f"present={present}")

    # Missingness checks
    if "name" in df.columns:
        non_null = df["name"].notna().mean()
        check("name_non_null_rate>=0.7", non_null >= 0.7, f"rate={non_null:.2f}")

    # Numeric sanity
    if "funding_total_usd" in df.columns:
        ok = (df["funding_total_usd"].dropna() >= 0).all()
        check("funding_total_usd_non_negative", ok, "")

    if "founded_year" in df.columns:
        years = df["founded_year"].dropna()
        if len(years) > 0:
            ok = ((years >= 1900) & (years <= 2026)).mean() >= 0.95
            check("founded_year_reasonable_range", ok, "expected mostly between 1900 and 2026")

    return report
