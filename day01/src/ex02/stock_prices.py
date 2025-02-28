import sys

def get_stock_price(company_name):
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
    
    company_name = company_name.title()
    ticker = COMPANIES.get(company_name)

    if ticker:
        return STOCKS.get(ticker)
    else:
        return None

def main():
    if len(sys.argv) != 2:
        return
    company_name = sys.argv[1]
    stock_price = get_stock_price(company_name)

    if stock_price is not None:
        print(stock_price)
    else:
        print("Unknown company")

if __name__ == "__main__":
    main()
