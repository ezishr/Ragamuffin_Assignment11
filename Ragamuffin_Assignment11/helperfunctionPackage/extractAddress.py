import re
from helperfunctionPackage.helperFunction import *
from zip_codePackage.zip_code import *

helper = HelperFunction(csv_link = './Data/fuelPurchaseData.csv')
ZipCodeAPI = ZipCodeAPI()
data, header = helper.read_CSV_file()
sample = data[0:4]

ohio_cities = [
    "Columbus",
    "Cleveland",
    "Cincinnati",
    "Toledo",
    "Akron",
    "Dayton",
    "Canton",
    "Youngstown",
    "Lorain",
    "Hamilton",
    "Springfield",
    "Elyria",
    "Lakewood",
    "Newark",
    "Middletown",
    "Dublin",
    "Mentor",
    "Mansfield",
    "Strongsville",
    "Cuyahoga Falls",
    "Fairfield",
    "Findlay",
    "Warren",
    "Lancaster",
    "Lima",
    "Westerville",
    "Lynchburg"
]

city_zipcode = {}
for city in ohio_cities:
    if city not in city_zipcode:
        city_zipcode[city] = ZipCodeAPI.request_api_zipcode(city = city, state_name = "Ohio")

address_idx = header.index("Full Address")

for row in sample:

    address_parts = row[address_idx].split(",")
    print(f'row:{row[address_idx]}\naddress_parts: {address_parts}')

    parts = [part for part in address_parts if not re.search(r'\d', part)]
    print(f'parts: {parts}')

    if len(parts) > 2:
         # Get first valid non-state 2-letter abbreviation as city
        city = next((part for part in parts if not re.fullmatch(r'[A-Z]{2}', part)), None)
        print(f'city: {city}')
        print(type(city))

        # true_zip_code = city_zipcode[city[0]][0]
        # print(true_zip_code)
        # new_address_parts = address_parts.copy()
        # new_address_parts = new_address_parts.append(true_zip_code)
        # print(f'new_address_parts: {new_address_parts}\n\n')
    else:
        city = parts[0] if parts else None
        print(f'city: {city}\n')
        print(f'current address: {address_parts}\n')

