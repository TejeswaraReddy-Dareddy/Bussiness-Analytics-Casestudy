# Case Study Report Draft
## Beyond the Headline Rate: A Data-Driven Transparency Scoring Framework for Advertised vs. Effective Interest Rates in the Indian Personal Loan Market

### 1. Problem Statement and Objectives
The approved proposal frames the problem as the difference between advertised personal-loan rates and the true cost after processing fees, foreclosure charges and other disclosed costs.

**Objectives**
1. Compute effective annualized borrowing cost for standardized personal-loan scenarios.
2. Quantify the gap between advertised rate and effective cost and identify cost components associated with the gap.
3. Compare the gap across public-sector banks, private banks and NBFCs and develop a reproducible transparency proxy.

### 2. Data Collection and Dataset Description
The current public-source seed snapshot contains 31 lenders from a Paisabazaar personal-loan comparison table. BankBazaar's public fees table can be used as a secondary source for charge validation.

The final analytical dataset contains standardized lender × loan amount × tenure scenarios. **These are derived scenarios, not 10,000 independent advertisements.** The report should say this explicitly.

Main fields:
- lender_name, lender_type
- loan_amount_inr, tenure_months
- advertised_rate_nominal_pct
- processing_fee_rate_pct, processing_fee_inr
- net_disbursed_inr, emi_inr, total_repayment_inr
- effective_apr_pct
- transparency_gap_pp
- fee_induced_gap_pp
- source_url, source_date

### 3. Data Preparation and Exploratory Analysis
Cleaning includes numeric conversion, lender-name normalization, rate-period normalization, missing-value handling, duplicate checks and source metadata retention.

Recommended visuals:
1. Advertised-rate distribution.
2. Effective-APR distribution.
3. Transparency-gap histogram.
4. Median gap by lender type.
5. Gap by loan amount tier.
6. Gap by tenure.

### APR methodology
For sanctioned principal P, processing fee F and GST G:

**Net disbursement = P − F − G**

The EMI is computed from the advertised reducing-balance interest rate. The effective monthly IRR is then solved using the net disbursed amount and the EMI cash flows.

**Effective APR = (1 + monthly IRR)^12 − 1**

RBI's KFS framework describes APR as an effective annualized rate computed on the net disbursed amount using an IRR/reducing-balance approach.

### Important assumptions
If a source publishes a fee as "up to 3%", the current model uses the published upper bound as a conservative scenario. It does not claim that every borrower pays 3%.

Foreclosure charges are excluded from the base APR because they are contingent on early closure and depend on timing/product conditions. They should be analyzed as a separate sensitivity case when the source gives enough information.

### 4. Analytics Method and Implementation
**Descriptive analytics:** mean, median, quartiles, standard deviation and distributions.

**Group comparison:** Kruskal-Wallis test for lender-type differences in gap.

**Multiple linear regression:** transparency gap as the dependent variable, with advertised rate, fee burden, loan amount, tenure and lender type as explanatory variables. Interpret as association, not causality.

**Transparency score:** combine lender median gap and gap variability. Lower gap and lower variability receive higher scores. The three proposal labels can be formed using sample terciles, but they are study-specific analytical tiers and not legal/regulatory findings.

### 5. State-of-the-Art Comparison

| Study | Dataset | Method | Evaluation | Relevance / comparison |
|---|---|---|---|---|
| Tantri & Vishen (2025) | Indian secured corporate loan contracts from MCA | Quasi-experimental transparency-policy analysis | Treatment/control lending-rate comparisons and robustness tests | Studies cost transparency and lending outcomes; this case study works at consumer offer/scenario level and computes effective APR. |
| Ali & Marisetty (2023; journal issue 2026) | ~2.19 million Google Play reviews of Indian FinTech loan apps | LDA/text analytics and probit models | Topic variables and prediction of flagged/fraud apps | Measures borrower experience and app quality; this case study measures price/cost transparency from public offer data. |
| Sidharta, Nurdina & Putri (2024) | Questionnaire from 272 fintech borrowers | Quantitative analysis of rate, administrative fee and risk | Statistical tests on loan-taking decisions | Uses borrower survey data; this case study uses public web data and standardized cost calculations. |

Do not compare studies using raw scores because datasets and experimental designs differ.

### 6. Results, Business Insights and Recommendations
**Update this section after the final scraper run. Do not invent results.**

Required result tables:
- Descriptive statistics.
- Median gap by lender type.
- Median fee-induced gap by lender type.
- Lender-level transparency score/tier.
- Regression coefficients.
- Sensitivity analysis.

**Recommendations**
- Comparison platforms should show effective borrowing cost alongside headline rate.
- Borrowers should compare net disbursement, EMI and total repayment, not rate alone.
- Lenders should expose fees in a standardized machine-readable format.
- Auditors/regulators could use automated recomputation as a screening mechanism.
- The score should be presented as an analytical signal, not a legal determination of misconduct.

### 7. Conclusion
The study creates a reproducible business-analytics workflow that converts public lender terms into standardized effective-cost scenarios. Its strongest methodological feature is the separation between scraped source terms and derived analytical scenarios.

### References
1. Reserve Bank of India. Key Facts Statement (KFS) for Loans & Advances, 15 April 2024.
2. Paisabazaar. Personal Loan — Interest Rates and Lender Comparison, accessed 25 September 2026.
3. BankBazaar. Personal Loan Fees and Charges, accessed 25 September 2026.
4. Tantri, P. & Vishen, N. (2025). *Does transparency about banks' lending costs lower firms' borrowing costs? Evidence from India*. Journal of Accounting and Economics, 79(2–3), 101737. DOI: 10.1016/j.jacceco.2024.101737.
5. Ali, A. & Marisetty, V. B. (2023/2026). *Are FinTech lending apps harmful? Evidence from user experience in the Indian market*. The British Accounting Review, 58(3), 101269. DOI: 10.1016/j.bar.2023.101269.
6. Sidharta, Y., Nurdina, N. & Putri, N. M. (2024). *The Effect of Interest Rate, Administrative Fees, and Risk on Online Lending Decisions on Fintech Lending Applications*. IJEBAR, 8(4). DOI: 10.29040/ijebar.v8i4.16178.
