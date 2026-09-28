# Custom Index Builder

A Python-based analytical application for creating a custom **Price Return Equity Index** from a predefined universe of 30 dummy stocks.

The application allows users to select stocks, choose a date range and weighting methodology, and generate an index with a base value of 100. The results are displayed through an interactive Streamlit interface.

## Visual Project Walkthrough

A visual walkthrough of the project architecture, methodology, application, and sample results will be available here:

**Notion Walkthrough:** `[Add link here]`

---

## Features

* Predefined universe of 30 dummy stocks
* Daily synthetic closing-price data
* Interactive stock selection
* Custom start and end dates
* Equal-weight methodology
* Float market-cap-weight methodology
* Price Return Index calculation
* Base index level of 100
* Cumulative return calculation
* Interactive index chart
* Input and data validation
* Automated tests using pytest

---

## Project Structure

```text
custom-index-builder/
│
├── app.py
│
├── data/
│   ├── stock.csv
│   └── prices.csv
│
├── src/
│   ├── __init__.py
│   ├── create_data.py
│   ├── create_prices.py
│   ├── data_loader.py
│   ├── validation.py
│   ├── returns.py
│   ├── weighting.py
│   ├── index_calculator.py
│   └── metrics.py
│
├── tests/
│   └── test_index.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Architecture

The project separates the user interface from the analytical logic.

```text
CSV Data
   ↓
Data Loading
   ↓
Validation
   ↓
Stock Return Calculation
   ↓
Weight Calculation
   ↓
Index Calculation
   ↓
Metrics
   ↓
Streamlit User Interface
```

The backend logic is divided into reusable Python modules instead of placing all calculations directly inside the Streamlit application.

---

## Data

The application uses synthetic data created specifically for this project.

### Stock Universe

`stock.csv` contains 30 dummy companies with:

* Ticker
* Company name
* Sector
* Float market capitalization

### Price Data

`prices.csv` contains daily synthetic closing prices with:

* Date
* Ticker
* Close price

The price dataset covers the same general date window for all securities.

---

## Index Methodology

This project implements a **Price Return Index**. Therefore, the index measures changes in stock prices and does not include dividends.

### 1. Stock Return

For each stock, the daily return is calculated as:

```text
Stock Return = Current Close Price / Previous Close Price - 1
```

### 2. Index Return

The daily index return is calculated as the weighted sum of constituent returns:

```text
Index Return = Σ (Stock Weight × Stock Return)
```

### 3. Index Level

The index starts with a base level of **100**.

Each subsequent index level is calculated as:

```text
New Index Level = Previous Index Level × (1 + Index Return)
```

---

## Weighting Methodologies

### Equal Weight

Every selected stock receives the same weight.

For example, if four stocks are selected:

```text
Weight of each stock = 1 / 4 = 25%
```

### Float Market-Cap Weight

Each stock receives a weight proportional to its float market capitalization:

```text
Stock Weight =
Stock Float Market Cap / Total Float Market Cap
```

The Streamlit application allows the user to choose between these two methodologies.

---

## Validation

The application performs checks before calculating the index.

These include:

* Required columns are present
* Stock and price datasets are not empty
* Missing values are detected
* Duplicate stock tickers are rejected
* Duplicate date-ticker price observations are rejected
* Close prices must be greater than zero
* Float market capitalization must be greater than zero
* Price tickers must exist in the stock universe
* At least one stock must be selected
* Start date must be before end date

The synthetic dataset generated for this project is designed to provide a consistent price history across the stock universe.

For a production implementation, missing observations would require an explicit methodology rather than silently filling values. One possible approach would be to exclude securities without sufficient price history for the requested period, warn the user, and recalculate the remaining constituent weights.

---

## Summary Metrics

The application displays:

* Starting Index Level
* Ending Index Level
* Cumulative Return

Cumulative return is calculated as:

```text
Cumulative Return =
Ending Index Level / Starting Index Level - 1
```

---

## Testing

Automated tests are implemented using `pytest`.

The tests verify:

* Equal-weight calculations
* Float market-cap-weight calculations
* Daily stock-return calculations
* Index-level calculations using known inputs

Run the tests using:

```bash
python -m pytest -v
```

---

## Installation

Clone the repository and move into the project directory.

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The main dependencies are:

* pandas
* NumPy
* Streamlit
* pytest

---

## Running the Application

From the project directory, run:

```bash
python -m streamlit run app.py
```

Streamlit will start a local server and open the Custom Index Builder in a web browser.

---

## Technology Stack

* Python
* pandas
* NumPy
* Streamlit
* pytest
* Git / GitHub
* CSV

---

## Limitations

This project is intentionally designed as a small analytical application.

Current limitations include:

* Synthetic rather than real market data
* Price Return only; dividends are not included
* No corporate-action adjustments
* No index rebalancing or reconstitution schedule
* Static float market-cap values
* No transaction costs
* No external database
* No production deployment

---

## Future Improvements

Possible extensions include:

* Real market-data integration
* Total Return Index calculation
* Corporate-action handling
* Historical market-cap changes
* Scheduled rebalancing and reconstitution
* Additional weighting methodologies
* More detailed performance and risk metrics
* Database integration
* Production deployment

---

## Design Philosophy

The project prioritizes simplicity, modularity, validation, and explainability.

The user interface is kept separate from the analytical backend so that the index methodology can be tested independently and extended without rewriting the entire application.
