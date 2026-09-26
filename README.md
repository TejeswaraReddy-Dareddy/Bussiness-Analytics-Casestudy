# Beyond the Headline Rate

## A Data-Driven Transparency Scoring Framework for Advertised vs. Effective Interest Rates in the Indian Personal Loan Market

**Data collection date:** 25 September 2026  
**Primary public source:** Paisabazaar personal-loan comparison page

### Important dataset description
This project contains **13,024 standardized analytical scenarios derived from 32 lender-level public terms**.

It is **not correct** to describe the 13,024 rows as 13,024 independent scraped advertisements.

Construction:
- 32 lender records from public comparison information
- 37 standardized loan amounts: ₹1,00,000 to ₹10,00,000 in ₹25,000 increments
- 11 standardized tenures: 12, 18, 24, 30, 36, 42, 48, 54, 60, 72 and 84 months
- 32 × 37 × 11 = **13,024 scenario observations**

### Problem statement
Advertised personal-loan rates do not by themselves describe the full borrowing cost. Upfront processing fees and GST can reduce the amount actually received while repayment is calculated on the sanctioned principal. This project standardizes published lender terms and calculates an effective annualized cost to quantify the gap between the headline rate and the scenario-level effective APR.

### Objectives
1. Quantify the gap between published advertised rate and scenario-level effective APR.
2. Examine how processing fees, loan amount and tenure relate to the gap.
3. Compare the distribution of the gap across public banks, private banks and NBFCs.
4. Construct a lender-level transparency score based on magnitude and consistency.

### Method
For each scenario:
1. Calculate processing fee according to the published rule.
2. Calculate 18% GST on the processing fee.
3. Calculate net disbursement.
4. Calculate EMI from the published nominal annual rate.
5. Solve for monthly IRR that equates net disbursement with the EMI stream.
6. Annualize the monthly IRR to obtain effective APR.
7. Compute `Transparency gap = Effective APR - Advertised rate`.

The lender score combines the percentile rank of median gap (80% weight) and gap variability (20% weight). The three tiers are **study-defined relative categories**, not legal, regulatory or consumer-protection findings.

### Current results
- Scenario observations: **13,024**
- Lenders: **32**
- Mean advertised rate: **10.70%**
- Mean effective APR: **14.19%**
- Median effective APR: **13.24%**
- Mean transparency gap: **3.50 percentage points**
- Median transparency gap: **2.58 percentage points**
- Lender-level Kruskal-Wallis: H = **18.407**, p = **0.000101**

### Structure
```text
├── README.md
├── analysis.ipynb
├── Case_Study_Report.pdf
├── SOURCE_NOTES.md
├── data/
│   ├── raw_source_lender_terms_2026-09-25.csv
│   └── scenario_dataset_13024_source_derived.csv
├── figures/
└── src/
    └── analysis_pipeline.py
```

### Limitations
- Public comparison pages publish indicative/start rates, not guaranteed borrower-specific offers.
- The scenario grid creates repeated observations from the same lender terms; inferential tests therefore use lender-level aggregation where appropriate, and regression errors are clustered by lender.
- Foreclosure/prepayment charges are not included in the base APR because they are conditional on borrower behavior/product terms.
- The transparency tiers are analytical classifications created for this study, not legal findings.

### State-of-the-art studies
1. Tantri & Vishen (2025), *Does transparency about banks' lending costs lower firms' borrowing costs? Evidence from India*, Journal of Accounting and Economics, 79(2–3), 101737.
2. Ali & Marisetty (2026 issue), *Are FinTech lending apps harmful? Evidence from user experience in the Indian market*, British Accounting Review, 58(3), 101269.
3. Sidharta, Nurdina & Putri (2024), *The Effect of Interest Rate, Administrative Fees, and Risk on Online Lending Decisions on Fintech Lending Applications*, IJEBAR, 8(4).

### Submission warning
The supplied proposal contains a different student's identity. This package therefore uses blank identity fields in the report. Replace them before submission.


## Machine Learning extension

The notebook also contains a three-model classification comparison for the study-defined transparency tier:

1. Logistic Regression
2. Random Forest
3. Gradient Boosting

Evaluation uses 5-fold Stratified Group Cross-Validation with lender name as the grouping variable. This prevents scenarios from the same lender appearing in both training and validation folds. Accuracy, precision, recall and weighted F1 are reported.

The ML predictors exclude effective APR, transparency gap, transparency score and transparency tier to avoid direct target leakage.
