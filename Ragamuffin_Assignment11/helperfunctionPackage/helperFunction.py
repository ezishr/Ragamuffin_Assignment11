# File Name: helperFunction.py
# Student Name: Annapoorna Nair
# Email: nairap@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date: April 15, 2025
# Course #/Section: IS 4010 - 001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Clean an excel sheet in a way the code can work with similar sheets
# Brief Description of what this module does: Make sure gross price will have 2 decimals & delete duplicate rows within excel after reading data
# Citations: Chatgpt helped with a lot of the code
# Anything else that's relevant: N/A

import csv
import re
from zip_codePackage.zip_code import *


class HelperFunction:
    """
    This class is used to read a CSV file and perform various operations on the data.
    """

    def __init__(self, csv_link):
        """
        Initialize the HelperFunction class with the CSV file link.
        @param csv_link string: The link to the CSV file.
        """
        self.csv_link = csv_link

    def read_CSV_file(self):
        '''
        Read the CSV file and return the data and header.
        @return: csv_data list: The data read from the CSV file.
        @return: header list: The header of the CSV file.
        '''
        csv_data = []
        with open(self.csv_link, newline='') as f:
            reader = csv.reader(f, delimiter=',')
            self.header = next(reader)
            for row in reader:
                csv_data.append(row)

        self.data = csv_data

        return csv_data, self.header

    def gross_price_two_decimals(self):
        """
        Make Gross Price column to have exactly 2 decimal places.
        @return data list: The data after being processed.
        """

        gross_price_idx = self.header.index('Gross Price')

        for row in self.data:
            row[gross_price_idx] = f"{float(row[gross_price_idx]):.2f}"

        return self.data


    def delete_duplicates(self):
        """
        NOT DONE
        Delete duplicate rows
        @return: excel data without any duplicate rows 
        """

        unique_rows = []
        seen = set()

        for i in range(len(self.data) - 1):
            row = self.data[i][1:].copy()
            print(f'index: {i}')
            row_tuple = tuple(row)  
            if row_tuple not in seen:
                unique_rows.append(self.data[i])
                seen.add(row_tuple)

            self.data = unique_rows
            print(f'seen len:{len(seen)}\nunique_rows len: {len(unique_rows)}')

        return seen, unique_rows


    def detect_pepsi(self):
        """
        Delete rows having Fuel Type of Pepsi and 
        write these rows into a CSV file named dataAnomalies.

        @return collected_row list: Data after being deleted with rows having Pepsi.
        """

        fuel_type_idx = self.header.index('Fuel Type')

        self.data = [row for row in self.data if row[fuel_type_idx].strip().lower() != 'pepsi']
        anomalies_row = [row for row in self.data if row[fuel_type_idx].strip().lower() == 'pepsi']
        with open('Data/dataAnomalies.csv', mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(self.header)
            writer.writerows(anomalies_row)

        return self.data

    def fix_address(self):
        """
        Fix the address by adding the zip code to the end of the address if there is no zip code.
        @return: data list: The data after address being fixed for first 5 rows.
        """

        zip_api = ZipCodeAPI()

        ohio_cities = [
            "Columbus",
            "Cleveland",
            "Cincinnati",
            "Circleville",
            'Clifton',
            "Bethel",
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
                city_zipcode[city] = zip_api.request_api_zipcode(city = city, state_name = "Ohio")

        address_idx = self.header.index("Full Address")

        count = 0

        while count <= 5:
            count += 1

            address_parts = self.data[count][address_idx].strip().strip(",").split(",")
            address_parts = [part.strip() for part in address_parts]
            zip_state_parts = [part for part in address_parts if not re.search(r'\d', part)]

            if len(zip_state_parts) > 1:
                city = next((part for part in zip_state_parts if not re.fullmatch(r'[A-Z]{2}', part)), None)

                true_zip_code = city_zipcode[city][0]

                new_address_parts = address_parts.copy()
                new_address_parts.append(str(true_zip_code))

                official_address = (", ").join(new_address_parts)

            else:
                official_address = ", ".join(address_parts)

            self.data[count][address_idx] = official_address

            # print(f'address: {self.data[count][address_idx]}\n\n')

        return self.data