import pandas as pd 
import numpy as np 
from pathlib import Path 

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

stock_file = DATA_DIR / "stock.csv"
prices_file = DATA_DIR / "prices.csv"

stock_df = pd.read_csv(stock_file)

print(stock_df.head())
print("number of stocks: " , len(stock_df))

dates = pd.bdate_range(
    start = "2024-01-01 " ,
    end = "2025-12-31"
)

print("first date : " , dates[0] )
print("last date : " , dates[-1] )
print("number of business days : " , len(dates))

rng = np.random.default_rng(42)

price_records = []

for ticker in stock_df["ticker"]:
    starting_price = rng.uniform(50 , 250) 

    daily_returns = rng.normal(

        loc = .0003 , 
        scale = .015 ,
        size = len(dates)
    )                      

    prices = starting_price  * np.cumprod(1+ daily_returns)

    for date,price in zip(dates,prices) : 
            price_records.append([
                 date,
                 ticker,
                 round(price , 2)
    ])

prices_df = pd.DataFrame(
      price_records ,
      columns= ["date" , "ticker" , "close_price"]
)
print(prices_df.head())
print(prices_df.shape)

# Basic price validation

print("missing value :")
print(prices_df.isna().sum())

print("number of tickers :" ,prices_df["ticker"].nunique())
print(" minimum price :" , prices_df["close_price"].min())

#data validation
assert prices_df["ticker"].nunique() == 30
assert prices_df["date"].notna().all()
assert prices_df["ticker"].notna().all()
assert prices_df["close_price"].notna().all()
assert (prices_df["close_price"] > 0).all()

print("Price data validation passed.")

prices_df.to_csv(
      prices_file , 
      index= False
)
print("prices.csv created successfully.")