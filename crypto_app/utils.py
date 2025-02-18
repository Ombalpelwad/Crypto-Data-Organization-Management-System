import requests


def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin,ethereum',
        'vs_currencies': 'usd',
        'include_market_cap': 'true',
        'include_24hr_vol': 'true',
        'include_24hr_change': 'true',
        'include_last_updated_at': 'true'
    }
    response = requests.get(url, params=params)
    data = response.json()
    # Reformat the data to match the requested structure
    detailed_data = {}
    for coin, values in data.items():
        detailed_data[coin] = {
            'usd': values.get('usd'),
            'usd_market_cap': values.get('usd_market_cap'),
            'usd_24h_vol': values.get('usd_24h_vol'),
            'usd_24h_change': values.get('usd_24h_change'),
            'last_updated_at': values.get('last_updated_at')
        }
    return detailed_data
