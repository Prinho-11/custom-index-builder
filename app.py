import streamlit as st

from src.data_loader import load_stocks, load_prices
from src.validation import validate_stocks, validate_prices
from src.returns import calculate_stock_returns
from src.weighting import (
    calculate_equal_weights,
    calculate_market_cap_weights
)
from src.index_calculator import calculate_index
from src.metrics import calculate_metrics

# Load and validate data

stocks = load_stocks()
prices = load_prices()

validate_stocks(stocks)
validate_prices(prices, stocks)

# Title and stock universe

st.title("Custom Index Builder")

st.write(
    "Select stocks, a date range, and a weighting method "
    "to create a custom Price Return Index."
)

st.subheader("Stock Universe")

st.dataframe(stocks)

# Let the user select stocks

selected_tickers = st.multiselect(
    "Select Stocks",
    options=stocks["ticker"].tolist(),
    default=stocks["ticker"].tolist()
)

# Weighting method

weighting_method = st.selectbox(
    "Select Weighting Method",
    [
        "Equal Weight",
        "Float Market Cap Weight"
    ]
)

# Date selection

min_date = prices["date"].min().date()
max_date = prices["date"].max().date()

start_date = st.date_input(
    "Start Date",
    value=min_date,
    min_value=min_date,
    max_value=max_date
)

end_date = st.date_input(
    "End Date",
    value=max_date,
    min_value=min_date,
    max_value=max_date
)

# generate button 

if st.button("Generate Index"):

    # First validate the user selection
    if len(selected_tickers) == 0:
        st.error("Please select at least one stock.")

    elif start_date >= end_date:
        st.error("Start date must be before end date.")

    else:
        selected_stocks = stocks[
            stocks["ticker"].isin(selected_tickers)
        ].copy()

        # Filter prices
        filtered_prices = prices[
            (prices["ticker"].isin(selected_tickers))
            &
            (prices["date"].dt.date >= start_date)
            &
            (prices["date"].dt.date <= end_date)
        ].copy()

        # Calculate returns
        returns = calculate_stock_returns(
            filtered_prices
        )

        # Choose weights
        if weighting_method == "Equal Weight":
            weights = calculate_equal_weights(
                selected_stocks
            )
        else:
            weights = calculate_market_cap_weights(
                selected_stocks
            )

        # Generate index + metrics
        index = calculate_index(
            returns,
            weights
        )

        metrics = calculate_metrics(index)

        # Display metrics
        st.subheader("Index Summary")

        st.metric(
            "Starting Index Level",
            f"{metrics['start_level']:.2f}"
        )

        st.metric(
            "Ending Index Level",
            f"{metrics['end_level']:.2f}"
        )

        st.metric(
            "Cumulative Return",
            f"{metrics['cumulative_return']:.2%}"
        )

        # Display chart
        st.subheader("Price Return Index")

        chart_data = index.set_index("date")[
            "index_level"
        ]

        st.line_chart(chart_data)