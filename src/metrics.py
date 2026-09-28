def calculate_metrics(index_df):

    start_level = index_df["index_level"].iloc[0]

    end_level = index_df["index_level"].iloc[-1]

    cumulative_return = (
        end_level / start_level - 1
    )

    return {
        "start_level": start_level,
        "end_level": end_level,
        "cumulative_return": cumulative_return
    }

if __name__ == "__main__":

    from data_loader import load_stocks, load_prices
    from returns import calculate_stock_returns
    from weighting import calculate_equal_weights
    from index_calculator import calculate_index

    stocks = load_stocks()
    prices = load_prices()

    returns = calculate_stock_returns(prices)
    weights = calculate_equal_weights(stocks)

    index = calculate_index(returns, weights)

    metrics = calculate_metrics(index)

    print(metrics)