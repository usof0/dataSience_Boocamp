import sys

def process_expression(expression):
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

    expression = expression.strip().title()
    if expression in COMPANIES:
        ticker = COMPANIES[expression]
        stock_price = STOCKS[ticker]
        return f"{expression} stock price is {stock_price}"
    
    ticker = expression.upper()
    if ticker in STOCKS:
        for company, symbol in COMPANIES.items():
            if symbol == ticker:
                return f"{ticker} is a ticker symbol for {company}"
    
    return f"{expression} is an unknown company or an unknown ticker symbol"

def main():
    if len(sys.argv) != 2:
        return
    
    input_string = sys.argv[1]
    
    if ',,' in input_string:
        return
    
    expressions = input_string.split(',')
    
    for expression in expressions:
        if expression.strip() == '':
            return

    for expression in expressions:
        result = process_expression(expression)
        print(result)

if __name__ == "__main__":
    main()
