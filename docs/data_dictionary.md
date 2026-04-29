# Data Dictionary Template

Use this file to document every important field in your dataset. A strong data dictionary makes your cleaning decisions, KPI logic, and dashboard filters much easier to review.

## How To Use This File

1. Add one row for each column used in analysis or dashboarding.
2. Explain what the field means in plain language.
3. Mention any cleaning or standardization applied.
4. Flag nullable columns, derived fields, and known quality issues.

## Dataset Summary

| Item | Details |
|---|---|
| Dataset name | UPI Transactions 2024 (Synthetic) |
| Source | Programmatically generated synthetic data inspired by NPCI, RBI, and India digital payments market patterns |
| Raw file name | `data/raw/upi_transactions_2024.csv` |
| Last updated | 2026-04-29 |
| Granularity | One row per transaction |

## Column Definitions

| Column Name | Data Type | Description | Example Value | Used In | Cleaning Notes |
|---|---|---|---|---|---|
| `transaction_id` | string | Unique transaction identifier | `TXN_2024_000001` | EDA / KPI / Tableau | Column renamed from `transaction id`; duplicate checks run (no duplicate IDs dropped in current run) |
| `timestamp` | datetime | Transaction date-time in 2024 | `2024-08-15 21:14:06` | EDA / KPI / Tableau | Parsed to datetime; used to validate/recompute temporal flags |
| `transaction_type` | string (categorical) | Payment type (`P2P`, `P2M`, `Bill Payment`, `Recharge`) | `P2M` | EDA / KPI / Tableau | Whitespace stripped and category normalized; unexpected values audited |
| `merchant_category` | string (categorical) | Merchant class for spending analysis | `grocery` | EDA / KPI / Tableau | Standardized to lowercase canonical labels; unexpected values flagged |
| `amount_inr` | float/int numeric | Transaction amount in INR | `1245.00` | EDA / KPI / Tableau | Renamed from `amount (INR)` and cast to numeric |
| `transaction_status` | string (categorical) | Processing outcome (`SUCCESS`, `FAILED`) | `SUCCESS` | EDA / KPI / Tableau | Trimmed and standardized; used to derive failure metrics |
| `sender_age_group` | string (categorical) | Sender age segment | `26-35` | EDA / KPI / Tableau | Text cleanup and category consistency checks |
| `receiver_age_group` | string (categorical) | Receiver age segment | `18-25` | EDA / KPI / Tableau | Text cleanup and category consistency checks |
| `sender_state` | string (categorical) | Sender state in India | `karnataka` | EDA / KPI / Tableau | Lowercased/trimmed; used in geo segmentation |
| `sender_bank` | string (categorical) | Sender bank name | `SBI` | EDA / KPI / Tableau | Category normalization and consistency checks |
| `receiver_bank` | string (categorical) | Receiver bank name | `HDFC` | EDA / KPI / Tableau | Category normalization and consistency checks |
| `device_type` | string (categorical) | Access channel (`Android`, `iOS`, `Web`) | `Android` | EDA / KPI / Tableau | Standardized labels; unexpected values audited |
| `network_type` | string (categorical) | Connectivity type (`3G`, `4G`, `5G`, `WiFi`) | `WiFi` | EDA / KPI / Tableau | Normalized alias mapping (for example `wi-fi` to `wifi`) |
| `fraud_flag` | Int64 (binary) | Fraud indicator (`1` fraud, `0` non-fraud) | `0` | EDA / KPI / Tableau | Cast to nullable integer; invalid binary checks applied |
| `hour_of_day` | Int64 | Hour extracted from timestamp | `21` | EDA / KPI / Tableau | Cast to nullable integer; used in time-of-day analysis |
| `day_of_week` | string (categorical) | Day label from timestamp | `Thursday` | EDA / KPI / Tableau | Standardized text categories; used for temporal slicing |
| `is_weekend` | Int64 (binary) | Weekend indicator (`1` Sat/Sun, `0` weekday) | `0` | EDA / KPI / Tableau | Recomputed from `timestamp`; mismatches corrected/flagged |

## Derived Columns

| Derived Column | Logic | Business Meaning |
|---|---|---|
| `failure_flag` | `1 if transaction_status == 'FAILED' else 0` | Core reliability KPI input (failed transactions and failure rate) |
| `is_peak_hour` | `1 if hour_of_day in [8-11, 19-22] else 0` | Enables peak vs off-peak reliability and fraud comparisons |
| `user_segment` | `sender_age_group + ' - ' + sender_state` | Composite segment for growth and user behavior clustering |
| `amount_category` | Bucket `amount_inr` into `Small (<500)`, `Medium (500-2K)`, `High (2K-10K)`, `Very High (>10K)` | Supports risk/value segmentation for fraud and growth dashboards |
| `value_bucket` | Bucket `amount_inr` into `Micro`, `Small`, `Medium`, `Large`, `Very Large` | Finer transaction value grouping for advanced analysis and dashboard filters |

## Data Quality Notes

- Standardization: raw column names converted to snake_case and string columns stripped of whitespace.
- Type corrections: `timestamp` parsed to datetime, numeric fields cast (`amount_inr`, `hour_of_day`, `fraud_flag`, `is_weekend`).
- Duplicate handling: exact duplicates and duplicate `transaction_id` rows checked; no removals in current cleaning output.
- Consistency rules: `is_weekend` recomputed from `timestamp`; binary validation applied to `fraud_flag` and `is_weekend`.
- Category hygiene: expected category checks for `merchant_category`, `device_type`, `network_type`, and other categorical fields; anomaly rows are auditable.
- Fraud baseline in dataset design is low (~0.2%), so segment-level fraud rates can be noisy for sparse groups.
- Output artifacts produced for dashboards:
  - `data/processed/cleaned_upi_transactions_2024.csv`
  - `data/processed/fraud_aggregated.csv`
  - `data/processed/reliability_aggregated.csv`
  - `data/processed/user_behavior_aggregated.csv`
