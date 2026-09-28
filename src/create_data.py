import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

print("data folder :", DATA_DIR)
print("project folder :", BASE_DIR)

stocks = [
    ("ALFA", "Alpha Technologies", "Technology"),
    ("BETA", "Beta Financials", "Financials"),
    ("GAMA", "Gamma Energy", "Energy"),
    ("DELT", "Delta Healthcare", "Healthcare"),
    ("EPSI", "Epsilon Consumer", "Consumer"),
    ("ZETA", "Zeta Industrials", "Industrials"),
    ("ETA", "Eta Communications", "Communication"),
    ("THET", "Theta Materials", "Materials"),
    ("IOTA", "Iota Utilities", "Utilities"),
    ("KAPP", "Kappa Technologies", "Technology"),

    ("LAMB", "Lambda Financials", "Financials"),
    ("MUON", "Muon Energy", "Energy"),
    ("NUXI", "Nuxi Healthcare", "Healthcare"),
    ("OMIC", "Omicron Consumer", "Consumer"),
    ("PIXX", "Pixx Industrials", "Industrials"),
    ("RHOX", "Rhox Communications", "Communication"),
    ("SIGM", "Sigma Materials", "Materials"),
    ("TAUX", "Taux Utilities", "Utilities"),
    ("UPSI", "Upsilon Technologies", "Technology"),
    ("PHIX", "Phi Financials", "Financials"),

    ("CHIX", "Chi Energy", "Energy"),
    ("PSIX", "Psi Healthcare", "Healthcare"),
    ("OMEG", "Omega Consumer", "Consumer"),
    ("ALTA", "Alta Industrials", "Industrials"),
    ("NOVA", "Nova Communications", "Communication"),
    ("ORBI", "Orbit Materials", "Materials"),
    ("VECT", "Vector Utilities", "Utilities"),
    ("CYGN", "Cygnus Technologies", "Technology"),
    ("LYRA", "Lyra Financials", "Financials"),
    ("AURA", "Aura Energy", "Energy"), ]

stock_df = pd.DataFrame(stocks, columns= ["ticker","company_name","sector"])



print(" no. of stocks :" , len(stock_df))
print("unique tickers :" , stock_df["ticker"].nunique())

rng = np.random.default_rng(42)

stock_df["float_market_cap"] =rng.integers(
    low=20_000 , high=2_00_000,
    size = len(stock_df)
)


assert len(stock_df) == 30 
assert stock_df["ticker"].nunique() == 30 
assert stock_df["ticker"].notna().all()
assert stock_df["company_name"].notna().all()
assert stock_df["sector"].notna().all()
assert (stock_df["float_market_cap"] > 0).all()
print(stock_df)
print("all stock validation passed")

stock_df.to_csv(
    DATA_DIR / "stock.csv" , 
    index = False )


print("stock.csv created successfully.")