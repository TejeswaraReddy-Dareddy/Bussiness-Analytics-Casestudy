# Beyond the Headline Rate

## Business Analytics Individual Case Study

This repository implements a web-data-driven analysis of advertised versus effective personal-loan borrowing costs in India.

### Data
The current seed snapshot contains 31 lender rows from a public Paisabazaar comparison table. The analysis expands lender terms into standardized loan-amount × tenure scenarios.

**Do not describe the expanded rows as 10,000 independent market advertisements.** They are derived analytical scenarios.

### Run
```bash
pip install pandas numpy scipy statsmodels matplotlib requests lxml
python src/scrape_paisabazaar.py
python src/build_scenario_dataset.py
jupyter notebook analysis.ipynb
```

Before final submission, rerun the scraper and keep the raw source tables, collection date/time, parsing steps, and assumptions.

### Files
- `README.md`
- `analysis.ipynb`
- `data/raw_lender_offers_seed.csv`
- `data/scenario_dataset_13860.csv`
- `src/scrape_paisabazaar.py`
- `src/build_scenario_dataset.py`
- `report/Case_Study_Report_Draft.md`
