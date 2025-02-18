Open your command prompt or terminal and Run the Django shell by executing:

--> python manage.py shell


Import and call your function within the shell:

>>>from crypto_app.utils import fetch_crypto_prices
>>>print(fetch_crypto_prices())