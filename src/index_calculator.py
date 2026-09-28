import pandas as pd

def calculate_index(returns_df, weights_df):

    merged_df = returns_df.merge(
        weights_df[["ticker", "weight"]],
        on="ticker"
    )

    merged_df["weighted_return"] = (
        merged_df["daily_return"] * merged_df["weight"]
    )

    index_df = (
        merged_df.groupby("date")["weighted_return"].sum().reset_index()

    )

    index_df = index_df.rename(columns={"weighted_return":"index_return"  })

    index_df["index_level"] = (
        100 * (1 + index_df["index_return"]).cumprod()
    )

    return index_df

if __name__ == "__main__":

    from data_loader import load_stocks, load_prices
    from returns import calculate_stock_returns
    from weighting import calculate_equal_weights

    stocks = load_stocks()
    prices = load_prices()

    returns = calculate_stock_returns(prices)
    weights = calculate_equal_weights(stocks)

    index = calculate_index(returns, weights)

    print(index.head(10))