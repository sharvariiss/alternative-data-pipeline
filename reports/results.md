# Alternative Data Pipeline Report

## Dataset Summary

- Raw shape: **54294 rows × 39 columns**
- Clean shape: **49439 rows × 39 columns**
- Output file: `data/processed/clean.csv`

## Validation Results

**Pipeline status:** ✅ PASSED

- ✅ non_empty_dataset — rows=49439
- ✅ has_any_key_columns — present=['name', 'market', 'category_list', 'status']
- ✅ name_non_null_rate>=0.7 — rate=1.00
- ✅ funding_total_usd_non_negative
- ✅ founded_year_reasonable_range — expected mostly between 1900 and 2026

## Top Missing Columns (percent)

|                     |   missing_% |
|:--------------------|------------:|
| funding_total_usd   |       99.92 |
| founded_year        |       22.16 |
| undisclosed         |        0    |
| equity_crowdfunding |        0    |
| convertible_note    |        0    |
| funding_rounds      |        0    |
| venture             |        0    |
| round_e             |        0    |
| round_b             |        0    |
| round_c             |        0    |
