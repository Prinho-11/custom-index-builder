from src.data_loader import load_prices , load_stocks

# First validation: empty stock universe
def validate_stocks(stock_df) : 
    if stock_df.empty: 
        raise ValueError("stock universe is empty.")
    # check required columns
    required_columns = [

        "ticker", "company_name" , "sector" , "float_market_cap"]

    for column in required_columns :
        if column not in stock_df.columns :
            raise ValueError (f"Missing required column : {column}")
    
    
    if stock_df[required_columns].isna().any().any() :
        raise ValueError("stock universe contains missing values.") 
    # validate duplicate tickers 
    if stock_df["ticker"].duplicated().any() :
        raise ValueError("duplicate tickers found in stock universe.")

    # validate market caps 
    if (stock_df["float_market_cap"] <= 0).any():
        raise ValueError("float market cap must be greater than zero. ")
    return  True




# Create validate_prices()

def validate_prices(prices_df, stock_df):

    if prices_df.empty:
        raise ValueError(
            "Price data is empty."
        )

    required_columns = [
        "date",
        "ticker",
        "close_price"
    ]

    for column in required_columns:

        if column not in prices_df.columns:
            raise ValueError(
                f"Missing required price column: {column}"
            )

    if prices_df[required_columns].isna().any().any():
        raise ValueError(
            "Price data contains missing values."
        )

    if (prices_df["close_price"] <= 0).any():
        raise ValueError(
            "Close prices must be greater than zero."
        )

    if prices_df.duplicated(
        subset=["date", "ticker"]
    ).any():

        raise ValueError(
            "Duplicate date-ticker observations found."
        )

    valid_tickers = set(stock_df["ticker"])
    price_tickers = set(prices_df["ticker"])

    unknown_tickers = price_tickers - valid_tickers

    if unknown_tickers:
        raise ValueError(
            f"Unknown tickers found: {unknown_tickers}"
        )

    

    return True

if __name__ == "__main__":

        stocks = load_stocks()
        prices = load_prices()

        validate_stocks(stocks)
        validate_prices(prices, stocks)

        print("Stock validation passed.")
        print("Price validation passed.")