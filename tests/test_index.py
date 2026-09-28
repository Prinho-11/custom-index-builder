import pandas as pd

from src.returns import calculate_stock_returns
from src.weighting import (
    calculate_equal_weights,
    calculate_market_cap_weights
)
from src.index_calculator import calculate_index

# test - 1 : If there are 2 stocks with equal weighting, does each receive 50%?

def test_equal_weights():

    stocks = pd.DataFrame({
        "ticker": ["AAA", "BBB"]
    })

    result = calculate_equal_weights(stocks)

    assert result["weight"].sum() == 1
    assert result["weight"].iloc[0] == 0.5
    assert result["weight"].iloc[1] == 0.5

# test-2 If AAA has market cap 100 and BBB has market cap 300, are the weights calculated correctly?


def test_market_cap_weights():

    stocks = pd.DataFrame({
        "ticker": ["AAA", "BBB"],
        "float_market_cap": [100, 300]
    })

    result = calculate_market_cap_weights(stocks)

    assert result["weight"].sum() == 1
    assert result["weight"].iloc[0] == 0.25
    assert result["weight"].iloc[1] == 0.75

# test -3 If a stock moves from ₹100 to ₹110, does our return function calculate 10%?

def test_stock_returns():

    prices = pd.DataFrame({
        "date": pd.to_datetime([
            "2025-01-01",
            "2025-01-02"
        ]),
        "ticker": ["AAA", "AAA"],
        "close_price": [100, 110]
    })

    result = calculate_stock_returns(prices)

    assert round(result["daily_return"].iloc[1], 2) == 0.10

# to test whether the code actually implements the assignment's weighted-return and index-level formulas correctly.

def test_index_calculation():

    returns = pd.DataFrame({
        "date": pd.to_datetime([
            "2025-01-01",
            "2025-01-01",
            "2025-01-02",
            "2025-01-02"
        ]),
        "ticker": ["AAA", "BBB", "AAA", "BBB"],
        "daily_return": [0.0, 0.0, 0.10, 0.20]
    })

    weights = pd.DataFrame({
        "ticker": ["AAA", "BBB"],
        "weight": [0.5, 0.5]
    })

    result = calculate_index(
        returns,
        weights
    )

    assert result["index_level"].iloc[0] == 100
    assert round(result["index_level"].iloc[1], 2) == 115.00