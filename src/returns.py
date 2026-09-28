import pandas as pd 


def calculate_stock_returns(prices_df) : 
    prices_df = prices_df.copy()

    prices_df = prices_df.sort_values(
        by=["ticker", "date"]
    )

    prices_df["daily_return"] = (
        prices_df.groupby("ticker")["close_price"].pct_change()
    )

    return prices_df

# testing 

if __name__ == "__main__":

    from data_loader import load_prices

    prices = load_prices()

    returns = calculate_stock_returns(prices)

    print(returns.head(10))

    