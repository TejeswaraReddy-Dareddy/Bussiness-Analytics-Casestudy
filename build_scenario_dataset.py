"""
Build the >10,000-row standardized scenario dataset.

These rows are analytical scenarios generated from public lender terms,
not 10,000 independent advertisements.
"""
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import brentq

GST = 0.18

def fee_amount(row, loan):
    if row["processing_fee_type"] == "fixed":
        return float(row["processing_fee_value"])
    return loan * float(row["processing_fee_value"]) / 100.0

def irr_monthly(net_disbursed, emi, n):
    def pv(r):
        if abs(r) < 1e-10:
            return emi*n
        return emi * (-np.expm1(-n*np.log1p(r))) / r
    return brentq(lambda r: pv(r)-net_disbursed, -0.99, 0.2)

def build(seed_path="data/raw_lender_offers_seed.csv",
          output_path="data/scenario_dataset.csv"):
    seed = pd.read_csv(seed_path)
    rows = []
    for _, row in seed.iterrows():
        max_loan = float(row["max_loan_lakh"]) * 100000
        amounts = np.unique(np.round(np.linspace(50000, max_loan, 20) / 1000) * 1000)
        for loan in amounts:
            for n in range(3, int(row["max_tenure_months"]) + 1, 3):
                fee = fee_amount(row, loan)
                gst = fee * GST
                net = loan - fee - gst
                rm = float(row["advertised_rate_annual_nominal"]) / 100 / 12
                emi = loan * rm * (1 + rm)**n / ((1 + rm)**n - 1)
                monthly_irr = irr_monthly(net, emi, n)
                apr = (1 + monthly_irr)**12 - 1
                baseline = (1 + rm)**12 - 1
                rows.append({
                    "lender_name": row["lender_name"],
                    "lender_type": row["lender_type"],
                    "loan_amount_inr": loan,
                    "tenure_months": n,
                    "advertised_rate_nominal_pct": row["advertised_rate_annual_nominal"],
                    "processing_fee_rate_pct": row["processing_fee_value"] if row["processing_fee_type"] != "fixed" else np.nan,
                    "processing_fee_inr": fee,
                    "gst_on_processing_fee_inr": gst,
                    "net_disbursed_inr": net,
                    "emi_inr": emi,
                    "total_repayment_inr": emi*n,
                    "baseline_effective_rate_pct": baseline*100,
                    "effective_apr_pct": apr*100,
                    "transparency_gap_pp": apr*100-row["advertised_rate_annual_nominal"],
                    "fee_induced_gap_pp": (apr-baseline)*100,
                    "processing_fee_type": row["processing_fee_type"],
                    "source_url": row["source_url"],
                    "source_date": row["source_date"],
                    "scenario_type": "standardized_grid_upper_fee_bound"
                })
    df = pd.DataFrame(rows)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print("Rows:", len(df))
    print("Lenders:", df["lender_name"].nunique())
    return df

if __name__ == "__main__":
    build()
