from helperfunctionPackage.readdata import *
from zip_codePackage.zip_code import *
import re
import requests


data, header = read_CSV_file(file_name = 'fuelPurchaseData.csv')
#print(f'header: {header}\n\nfirst row: {data[0:8]}')

data = gross_price_two_decimals(data)

data = detect_pepsi(data, header)

zip_code = request_api_zipcode(city = 'Cincinnati', state_name = 'Ohio')
print(zip_code)

print(data[0])


# NEED: function to get rows missing zip code

def update_missing_zip_codes(data, header):
    updated_rows = 0
    zip_index = header.index('zip')
    city_index = header.index('city')
    state_index = header.index('state')

    for row in data:
        if not row[zip_index]:  # missing zip code
            city = row[city_index]
            state = row[state_index]
            zip_code = request_api_zipcode(city, state)
            if zip_code:
                row[zip_index] = zip_code
                updated_rows += 1
    print(f"Updated {updated_rows} rows with missing ZIP codes.")
    return data

# 5. Run update
data = update_missing_zip_codes(data, header)