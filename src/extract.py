import requests


def get_quotes_stock(email,product="stocks",country="brazil", code="RADL3", start_date ="09/27/2022", end_date="07/18/2023"):
    """
    Official documentation: http://api.scraperlink.com/investpy/

    Overview:
    Fetches historical stock quotes using the Investpy API through the specified proxy service.

    Parameters:
    - product (str): Type of financial product (default is "stock").
    - country (str): Country of the financial product (default is "brazil").
    - code (str): Symbol, ID, or name of the financial product (default is "RADL3").
    - start_date (str): Start date for historical data in the format "MM/DD/YYYY" (default is "09/27/2022").
    - end_date (str): End date for historical data in the format "MM/DD/YYYY" (default is "07/18/2023").

    Returns:
    - dict: Historical data in JSON format.

    Example:
    ```python
    # Example for Stocks
    data_stocks = get_quotes_stock(product="stocks", country="united states", code="TSLA", start_date="09/27/2022", end_date="09/28/2022")
    ```
    """
    url=f"http://api.scraperlink.com/investpy/?email={email}&"+\
        "type=historical_data&" +\
        f"product={product}&" +\
        f"country={country}&" +\
        f"symbol={code}&" +\
        f"from_date={start_date}&" +\
        f"to_date={end_date}&" +\
        f"time_frame=Daily"
    response = requests.get(url)
    if response.status_code == 200:
        # The request was successful.
        data = response.json()
        return data
    else:
        # The request was not successful.
        print(response.status_code)
        print(response.text)
        print(url)
        return url
    
def get_crypto_stock(email:str, symbol:str,start_date ="09/27/2022", end_date="07/18/2023"):
    """
    Example:
    ```python
    # Example for crypto
    crypto_stock = get_quotes_stock(email=email, symbol=BTC, start_date="09/27/2022", end_date="09/28/2022")
    ```
    """
    url=f"http://api.scraperlink.com/investpy/?email={email}"+\
    f"&type=historical_data&product=cryptos&symbol={symbol}&from_date={start_date}&"+\
    f"to_date={end_date}"
    
    response = requests.get(url)
    if response.status_code == 200:
        # The request was successful.
        data = response.json()
        return data
    else:
         # The request was not successful.
        raise ValueError(f"HTTP status code:{response.status_code}.   {response.text}")