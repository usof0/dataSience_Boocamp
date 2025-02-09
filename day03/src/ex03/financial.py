import sys
import time
import requests
from bs4 import BeautifulSoup

def get_financial_data(ticker, field):
    time.sleep(5)
    url = f"https://finance.yahoo.com/quote/{ticker}/financials/?p={ticker}"

    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch data: {e}")
    
    soup = BeautifulSoup(response.text, 'html.parser')

    table_data = soup.find('div', {'class': 'tableBody yf-9ft13'})
    if not table_data:
        raise Exception(f"No data found for {ticker}")
    
    rows = table_data.find_all('div', {'class': 'row lv-0 yf-t22klz'})
    if not rows:
        raise Exception(f"No data found for {ticker}")
    
    for row in rows:
        row_title = row.find('div', {'class': 'rowTitle yf-t22klz'})
        if row_title and field.lower() in row_title.text.strip().lower():
            cells = row.find_all('div', {'class': 'column yf-t22klz'}) + \
                    row.find_all('div', {'class': 'column yf-t22klz alt'})
            values = tuple(cell.get_text(strip=True) for cell in cells)
            return values
        
        raise Exception(f"Field {field} not found for {ticker}")

def main():
    try:
        if len(sys.argv) != 3:
            raise ValueError("Usage: python3 financial.py <ticker_symbol> <field_of_the_table>")
        
        ticker_symbol = sys.argv[1]
        field = sys.argv[2]
        
        result = get_financial_data(ticker_symbol, field)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    
if __name__ == "__main__":
    main()
    