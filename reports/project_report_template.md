# UPI Transaction Intelligence 2024

---

## 1. Cover Page

- **Project Title:** UPI Transaction Intelligence 2024  
- **Sector:** FinTech / Digital Payments  
- **Team ID and Members:** _[Add details]_  
- **Faculty Mentor:** _[Add details]_  
- **Institute:** _[Add details]_  
- **Submission Date:** _[Add date]_  

---

## 2. Executive Summary

The system processes ~250,000 transactions with an overall success rate of ~95%.

Fraud remains low (~0.19%) but is **concentrated in high-value transactions and specific user segments**, indicating risk is behavior-driven rather than volume-driven.

Reliability shows a **stable failure baseline (~5%)**, but transaction flow is **structurally centralized**, with SBI handling ~25% of traffic, making system performance dependent on a few high-volume nodes.

Growth is driven by **core cohorts (26–45 age group)** contributing most of the value, while younger users (18–25) drive engagement but lower transaction value.

### Key Recommendations

- Strengthen fraud detection for **high-value and high-risk segments**
- Design infrastructure to **handle persistent load concentration on dominant banks**
- Focus growth on **core segments while expanding underpenetrated cohorts**

---

## 3. Sector and Business Context

### Fraud
- Digital payments face increasing fraud sophistication  
- Stakeholders: Risk teams, compliance teams, regulators  
- Critical for maintaining trust and regulatory compliance  

### Reliability
- UPI operates as a **real-time distributed system**  
- Stakeholders: NPCI, banking infrastructure teams, SRE teams  
- Critical for uptime, throughput, and user experience  

### Growth
- Growth driven by adoption, transaction frequency, and merchant ecosystem  
- Stakeholders: Product teams, business teams, partnerships  
- Critical for scaling ecosystem value  

---

## 4. Problem Statement and Objectives

### Fraud
Identify **high-risk segments and transaction behaviors**

### Reliability
Understand **system load distribution and dependency patterns**

### Growth
Identify **high-value users and expansion opportunities**

---

## 5. Data Description

- Synthetic dataset (~250,000 transactions)  
- Covers full 2024 calendar  
- Includes demographics, banks, network, device, and transaction details  

### Key Columns

- Time: `timestamp`, `hour_of_day`, `day_of_week`  
- Transaction: `amount_inr`, `transaction_type`, `merchant_category`  
- Segments: `sender_bank`, `receiver_bank`, `age_group`, `state`  
- Risk: `fraud_flag`  

### Data Limitations

- Synthetic nature limits causal inference  
- Sparse fraud labels  
- No infrastructure-level metrics  

---

## 6. Cleaning and Transformation

- Standardized column formats and types  
- Parsed timestamps and derived time features  
- Created:
  - `failure_flag`
  - `is_peak_hour`
  - `amount_bucket`
  - `user_segment`

---

## 7. KPI Framework

### Fraud
- Fraud Rate = Fraud Txns / Total Txns  
- Avg Fraud Value  
- Outlier Fraud %  

### Reliability
- Success Rate  
- Avg Throughput (transactions/hour)  
- Peak Throughput  

### Growth
- Avg Transaction Value  
- Segment Contribution  
- Transactions per Segment  

---

## 8. Exploratory Analysis

### Fraud
- Fraud is **not evenly distributed**
- Higher in **high-value transactions (>10K)**
- Certain age groups and regions show higher concentration  

### Reliability
- Failure rate remains **uniform (~5%) across all dimensions**
- Load shows clear peaks: **10AM–1PM and 5PM–9PM**
- Transaction flow is **centralized**, with SBI dominating both sender and receiver roles  

### Growth
- 26–45 age group drives majority of value  
- 18–25 shows high engagement but lower transaction value  
- Value is concentrated in mid-to-high transaction ranges  

---

## 9. Statistical Analysis

### Fraud
- Fraud probability increases with transaction value  
- Minimal dependence on time → indicates opportunistic behavior  

### Reliability
- No significant variation across segments  
- Indicates **system-wide behavior rather than localized issues**  
- Load distribution reveals **centralized routing dependency**

### Growth
- Core segments dominate value contribution  
- Long-tail users contribute low volume  

---

## 10. Dashboard Walkthrough

### Fraud Dashboard
- Identifies **risk concentration across segments**
- Highlights **high-value and high-risk transaction patterns**

### Reliability Dashboard
- Shows **time-based load distribution**
- Identifies **SBI as dominant routing node**
- Heatmap reveals **high-volume bank interaction paths**

### Growth Dashboard
- Segments users by **value and engagement**
- Identifies **core vs growth vs low-priority segments**

---

## 11. Key Insights

### Fraud
- High-value transactions show **higher fraud probability**
- Fraud is **segment-driven, not volume-driven**
- Risk concentrated in specific demographics and regions  

### Reliability
- System maintains **stable ~5% failure rate**
- SBI handles ~25% of total traffic  
- Reliability depends on **few high-volume nodes, not uniform distribution**

### Growth
- 26–45 is the **core value segment**
- 18–25 is the **engagement segment**
- Growth opportunity exists in **underutilized segments and regions**

---

## 12. Recommendations

### Fraud
- Focus monitoring on **high-value transactions**
- Implement **segment-aware fraud detection models**
- Target high-risk regions and demographics  

### Reliability
- Design systems assuming **persistent load concentration**
- Implement **adaptive retry and throttling mechanisms**
- Monitor **critical bank-pair interaction paths**

### Growth
- Strengthen engagement in **core segments**
- Expand into **low-engagement cohorts**
- Optimize high-frequency transaction categories  

---

## 13. Limitations and Next Steps

### Limitations
- Synthetic dataset limits real-world applicability  
- Missing infrastructure metrics (latency, retries, failures)  
- Fraud signals are simplified  

### Next Steps
- Integrate real-time system metrics  
- Build predictive load models  
- Conduct controlled experiments for growth strategies  

---

## Final Positioning

**The system demonstrates stable performance but is structurally centralized — operational reliability depends on a few dominant nodes, while fraud and growth patterns remain segment-driven.**

---

## 14. Contribution Matrix

- Data Engineering: _[Add details]_  
- Fraud Analysis: _[Add details]_  
- Reliability Analysis: _[Add details]_  
- Growth Analysis: _[Add details]_  
- Dashboard Development: _[Add details]_  
- Report Writing: _[Add details]_  