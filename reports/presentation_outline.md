# UPI Transaction Intelligence 2024 — Presentation Script
## Presentation Link: https://drive.google.com/drive/folders/1n0KhEmAv-02wujuHO21iTn-8O-wR0TmH?usp=sharing

## Slide 1 — Title

Hi, we are presenting **UPI Transaction Intelligence 2024**, where we analyze fraud risk, system reliability, and growth patterns in a unified framework.

---

## Slide 2 — Context and Problem Statement

UPI is a high-volume, real-time payment system where three things matter simultaneously:
- Fraud prevention  
- System reliability  
- User and transaction growth  

These objectives often conflict.  
Stronger fraud controls can reduce success rates, while weaker controls increase risk.

Our goal:
**Build a unified framework to analyze fraud, reliability, and growth together, not in silos.**

---

## Slide 3 — Data Engineering

We worked with a synthetic dataset of ~250,000 transactions covering the full year.

Key steps:
- Standardized schema and cleaned inconsistencies  
- Parsed timestamps and derived time-based features  
- Created analytical fields like:
  - `failure_flag`
  - `is_peak_hour`
  - `amount_bucket`
  - `user_segment`

This ensures a consistent base for all three dashboards.

---

## Slide 4 — KPI Framework

We defined a shared KPI layer across all dashboards.

### Fraud
- Fraud Rate  
- Fraud Amount  
- Outlier Fraud %

### Reliability
- Success Rate  
- Avg Throughput (transactions/hour)  
- Peak Throughput  

### Growth
- Avg Transaction Value  
- Segment Contribution  
- Transaction Volume  

This allows all teams to work with a **common decision language**.

---

## Slide 5 — Key EDA Insights

### Fraud
- Fraud is higher in **high-value transactions**
- Outliers contribute disproportionately to fraud

### Reliability
- Failure rate is stable (~5%) across all segments  
- No clear failure hotspots across time, network, or banks  

### Growth
- 26–45 age group drives most value  
- 18–25 drives high engagement but lower value  

---

## Slide 6 — Advanced Analysis

We performed segmented comparisons across:
- Age groups  
- Banks  
- Transaction value  
- Time  

### Key findings:
- Fraud is **behavior-driven, not volume-driven**
- Reliability is **system-wide, not segment-specific**
- Growth is **concentrated in core cohorts**

---

## Slide 7 — Dashboard Overview

We built three dashboards:

### Fraud Dashboard
- Focus: Risk concentration across segments  

### Reliability Dashboard
- Focus: System load and routing behavior  

### Growth Dashboard
- Focus: User segmentation and value contribution  

Each dashboard supports **operational decision-making**.

---

## Slide 8 — Top Insights

### Fraud
- High-value transactions carry higher fraud risk  

### Reliability
- System maintains stable performance (~5% failure rate)  
- But transaction flow is **centralized**  
- SBI handles ~25% of total traffic → key dependency  

### Growth
- 26–45 = value core  
- 18–25 = engagement core  
- Clear opportunity for upselling  

---

## Slide 9 — Recommendations

### Fraud
- Focus monitoring on high-value transactions  
- Use segment-aware risk scoring  

### Reliability
- Design systems to handle **persistent load concentration**  
- Focus on **high-volume routing paths (e.g., SBI interactions)**  
- Implement retry and throttling strategies  

### Growth
- Strengthen core segments  
- Expand into underutilized cohorts  
- Optimize high-frequency transaction categories  

---

## Slide 10 — Impact

Expected outcomes:
- Reduced fraud exposure  
- Improved system stability  
- Better monetization per user  

Priority:
1. Fraud controls on high-value transactions  
2. Reliability monitoring on high-load paths  
3. Growth strategies for key segments  

---

## Slide 11 — Limitations

- Dataset is synthetic  
- No infrastructure-level metrics (latency, retries)  
- Insights are diagnostic, not causal  

---

## Slide 12 — Next Steps

- Integrate real-time system metrics  
- Build anomaly detection systems  
- Run controlled experiments for growth  

---

## Final Closing Line

The system is stable, but structurally centralized —  
**reliability depends on a few dominant nodes, while fraud and growth remain segment-driven.**