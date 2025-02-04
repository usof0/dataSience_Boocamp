import sys

def get_company_and_stock_price(ticker_symbol):
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    ticker_symbol = ticker_symbol.upper()
    stock_price = STOCKS.get(ticker_symbol)

    if stock_price is not None:
        for company, symbol in COMPANIES.items():
            if symbol == ticker_symbol:
                return company, stock_price
    else:
        return None
    
def main():
    if len(sys.argv) != 2:
        return
    
    ticker_symbol = sys.argv[1]
    result = get_company_and_stock_price(ticker_symbol)
    
    if result is not None:
        company, stock_price = result
        print(f"{company} {stock_price}")
    else:
        print("Unknown company")

if __name__ == "__main__":
    main()
