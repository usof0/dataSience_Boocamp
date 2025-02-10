import pytest
from financial import get_financial_data

def test_correct_output():
    ticker = "MSFT"
    field = "Total Revenue"
    result = get_financial_data(ticker, field)

    assert result == ('245,122,000.00', '198,270,000.00', '261,802,000.00', '211,915,000.00', '168,088,000.00'), "The result should be:\
    ('245,122,000.00', '198,270,000.00', '261,802,000.00', '211,915,000.00', '168,088,000.00')"

def test_type_of_output():
    ticker = "MSFT"
    field = "Total Revenue"
    result = get_financial_data(ticker, field)

    assert isinstance(result, tuple), "The result should be a tuple"

def test_invalid_ticker():
    ticker = "MSFTtttttttt"
    field = "Total Revenue"
    with pytest.raises(Exception) as exc_info:
        get_financial_data(ticker, field)
    assert f"No data found for {ticker}" in str(exc_info.value), "An exception should be raised for an invalid ticker."
