import pandas as pd 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

stock_file = DATA_DIR / "stock.csv"
prices_file = DATA_DIR / "prices.csv" 

#functions

def load_stocks() : 
    stock_df = pd.read_csv(stock_file)
    return stock_df

def load_prices() :
    prices_df = pd.read_csv(
        prices_file , 
        parse_dates= ["date"])

    return prices_df

if  __file__ == "__main__" : 
    stocks = load_stocks()
    prices = load_prices()

    print(stocks.head())
    print()
    print(prices.head())

    print()
    print(stocks.dtypes)
    print()
    print(prices.dtypes)


