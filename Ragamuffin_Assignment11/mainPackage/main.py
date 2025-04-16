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

