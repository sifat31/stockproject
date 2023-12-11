import os
import django
import json
import locale
from decimal import Decimal

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockproject.settings')
django.setup()

from stockapp.models.json_models import JsonModel

def load_data():
    # Set the locale to handle comma as a thousand separator
    locale.setlocale(locale.LC_NUMERIC, '')

    with open('stock_market_data.json', 'r') as file:
        data = json.load(file)
        for item in data:
            try:
                # Use locale.atof to handle the conversion
                volume = Decimal(locale.atof(item['volume']))
            except ValueError:
                volume = Decimal(0)

            high = Decimal(locale.atof(item['high']))
            low = Decimal(locale.atof(item['low']))
            open_value = Decimal(locale.atof(item['open']))
            close = Decimal(locale.atof(item['close']))

            JsonModel.objects.create(
                date=item['date'],
                trade_code=item['trade_code'],
                high=high,
                low=low,
                open=open_value,
                close=close,
                volume=volume
            )

if __name__ == "__main__":
    load_data()
