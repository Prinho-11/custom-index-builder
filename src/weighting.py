# Equal weighting 

def calculate_equal_weights(stock_df):

    number_of_stocks = len(stock_df)

    stock_df = stock_df.copy()

    stock_df["weight"] = 1 / number_of_stocks

    return stock_df

#Market-cap weighting

def calculate_market_cap_weights(stock_df):

    stock_df = stock_df.copy()

    total_market_cap = stock_df["float_market_cap"].sum()

    stock_df["weight"] = (
        stock_df["float_market_cap"] / total_market_cap
    )

    return stock_df

if __name__ == "__main__":

    from data_loader import load_stocks

    stocks = load_stocks()

    equal_weights = calculate_equal_weights(stocks)

    print("Equal Weights:")
    print(equal_weights[["ticker", "weight"]].head())

    market_cap_weights = calculate_market_cap_weights(stocks)

    print()
    print("Market Cap Weights:")
    print(
        market_cap_weights[
            ["ticker", "float_market_cap", "weight"]
        ].head()
    )

    print()
    print("Equal weight total:")
    print(equal_weights["weight"].sum())

    print("Market cap weight total:")
    print(market_cap_weights["weight"].sum())

