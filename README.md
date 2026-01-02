# Alternative Data Pipeline for Research & Analytics

## Overview
This project implements a **reproducible, end-to-end data pipeline** for research and analytics use cases.
It demonstrates how raw, real-world datasets can be ingested, cleaned, validated, and transformed into
**analysis-ready data**, with automated reporting for transparency and reliability.

The pipeline is intentionally lightweight and interpretable, reflecting how **alternative datasets**
(such as startup, market, or investment data) are prepared before being used in downstream
machine learning, analytics, or venture research workflows.

---

## Why This Project Matters
In real-world data science and quantitative research, **data quality is often more critical than modeling**.
This project shows the ability to:

- Handle large, messy, real-world datasets
- Design reproducible and maintainable data pipelines
- Apply systematic data quality and validation checks
- Produce automated, human-readable reports for stakeholders

These skills are essential in **research, analytics, and venture environments**, where decisions depend
on trustworthy data rather than isolated experiments.

---

## Dataset
- Crunchbase-style startup investment dataset
- Size: ~54,000 records across 39 columns
- Characteristics:
  - Mixed data types (text, numeric, categorical)
  - Missing and sparse values
  - Real-world inconsistencies typical of alternative data

> Raw data is intentionally excluded from version control.  
> Only cleaned outputs and generated reports are tracked.

---

## Pipeline Architecture

data/raw → ingestion
↓
cleaning & standardization
↓
data validation checks
↓
data/processed → clean.csv
↓
reports → results.md



---

## Pipeline Steps

### 1. Ingestion
- Loads raw CSV data from disk
- Robust handling of non-UTF8 encodings (common in Kaggle / Windows exports)

### 2. Cleaning
- Standardizes column names
- Removes duplicate rows
- Trims text fields
- Coerces numeric columns where applicable
- Preserves data integrity while improving usability

### 3. Validation
The pipeline applies several data quality checks:
- Dataset is non-empty
- Presence of key columns (e.g. name, market, category, status)
- Minimum non-null thresholds for important fields
- Sanity checks for numeric ranges (e.g. founded year, funding values)

Each validation produces a **pass/fail signal** used in reporting.

### 4. Reporting
An automated markdown report is generated containing:
- Dataset shape before and after cleaning
- Validation results and status
- Summary of missing values (top columns by percentage)

This makes data quality transparent and reviewable.

---

## Outputs
- `data/processed/clean.csv`  
  → Cleaned, analysis-ready dataset

- `reports/results.md`  
  → Automated pipeline report including validation checks and missingness analysis

---

## How to Run

From the project root (with an activated virtual environment):

```bash
pip install -r requirements.txt
python -m src.run_pipeline
