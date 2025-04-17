# File Name: helperFunction.py
# Student Name: Annapoorna Naire, Eirlys Vo
# Email: nairap@mail.uc.edu, vopq@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date: April 17, 2025
# Course #/Section: IS 4010 - 001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Clean provided CSV data file in a way the code can work with similar data file.
# Brief Description of what this module does: Focus on working with data for assignment 11.
# Citations: ChatGPT with regular expression 
# Anything else that's relevant: N/A

from WriteToCSVPackage.write_to_csv import *
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

        # Initialize attribute csv_link from the provided parameter csv_link.
        self.csv_link = csv_link

    def read_CSV_file(self):
        '''
        Read the CSV file and return the data and header.
        @return: csv_data list: The data read from the CSV file.
        @return: header list: The header of the CSV file.
        '''

        csv_data = [] # Initialize list object to store data.
        
        # Use with open to read CSV file.
        with open(self.csv_link, newline='') as f:
            reader = csv.reader(f, delimiter=',')
            self.header = next(reader) # Store header from CSV file into header attribute.

            # Loop through each row and add to csv_data
            for row in reader:
                csv_data.append(row)
        
        # Initialize data attribute to store csv_data object.
        self.data = csv_data

        return csv_data, self.header


    def gross_price_two_decimals(self):
        """
        Make Gross Price column to have exactly 2 decimal places.
        @return data list: The data after being processed.
        """

        # Get index of Gross Price column from header attribute.
        gross_price_idx = self.header.index('Gross Price')

        # Loop through each row and force the format to be 2 decimal places.
        for row in self.data:
            row[gross_price_idx] = f"{float(row[gross_price_idx]):.2f}"

        return self.data


    def delete_duplicates(self):
        """
        Remove duplicated rows from the original data.
        @return data list: Data after being deleted from duplicated rows.
        """

        unique_rows = [] # List type to store unique rows from data.
        seen = set() # Set type to check duplicate rows.

        # Loop through each row using index. 
        for row in self.data:
            
            row_tuple = tuple(row[1:]) # Make the row to be tuple type for checking purpose.

            # If the row_tuple is not in the seen (set), the original row will be added to unique_rows and row_tuple is added to seen (set).
            if row_tuple not in seen:
                unique_rows.append(row)
                seen.add(row_tuple)

        # Restore the unique_rows back to data attribute.
        self.data = unique_rows

        return self.data


    def detect_pepsi(self):
        """
        Delete rows having Fuel Type of Pepsi and 
        write these rows into a CSV file named dataAnomalies.

        @return collected_row list: Data after being deleted with rows having Pepsi.
        """

        # Get the index of Fuel Type column.
        fuel_type_idx = self.header.index('Fuel Type')

        # List comprehesion: loop through each row and check Fuel Type item if it's Pepsi or not, store only the True ones.
        anomalies_row = [row for row in self.data if row[fuel_type_idx].strip().lower() == 'pepsi']

        # List comprehesion: loop through each row and check Fuel Type item if it's Pepsi or not, store only the False ones.
        self.data = [row for row in self.data if row[fuel_type_idx].strip().lower() != 'pepsi']
        
        # Write the anomalies_row into CSV data file and save in Data folder.
        to_csv = Write_To_CSV(path = 'Data/dataAnomalies.csv', data = anomalies_row, header = self.header)
        to_csv.write_to_csv_path()

        return self.data


    def fix_address(self):
        """
        Fix the address by adding the zip code to the end of the address if there is no zip code.
        @return: data list: The data after address being fixed for first 5 rows.
        """

        # Initialize zip code API.
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

        city_zipcode = {} # Dictionary object to save city names as keys and zip code list as values

        # Loop through each city name in ohio_cities above and use zip_api to find the zip code list.
        for city in ohio_cities:
            if city not in city_zipcode:
                city_zipcode[city] = zip_api.request_api_zipcode(city = city, state_name = "Ohio")

        # Get index of column Full Address
        address_idx = self.header.index("Full Address")

        # count variable to help track only find first 5 missing zip code rows.
        # idx variable to track index when looping rows.
        count, idx = 0, 0

        while (count <= 5) and (idx <= len(self.data)):

            # Extract Full Address into parts separated by comma.
            address_parts = self.data[idx][address_idx].strip().strip(",").split(",")
            address_parts = [part.strip() for part in address_parts] # Remove space at the beginning and ending of the extracted parts.
            
            # Get parts that don't have digits in that string. 
            # For example, "4232 Cougar Parkwy, Lynchburg, OH" is extracted to ["4232 Cougar Parkwy", "Lynchburg", "OH"] and there are parts ["Lynchburg", "OH"] that don't have numbers inside.
            zip_state_parts = [part for part in address_parts if not re.search(r'\d', part)]

            # If the zip_state_parts has more than 1 items, meaning that the state is in the string with zip code and that address already has zip code.
            # Example: "43251 OH,  Columbus, 3099 Daylight Street," -> "43251 OH" part has state and zip code already.
            if len(zip_state_parts) > 1:
                count += 1 # count is incremented by 1 since we just fix zip code for first 5 found rows.

                # Use regular expression to extract the city from part that has 2 capitalized letters.
                city = next((part for part in zip_state_parts if not re.fullmatch(r'[A-Z]{2}', part)), None)

                # Get the first zip code from that city using the above city_zipcode.
                true_zip_code = city_zipcode[city][0]

                # Append the zip code part into list of address parts and join them by comma
                new_address_parts = address_parts.copy()
                new_address_parts.append(str(true_zip_code))

                official_address = (", ").join(new_address_parts)

            else:
                official_address = ", ".join(address_parts) # Join back to string of full address for those that already have zip code.

            # Update full address
            self.data[idx][address_idx] = official_address
            idx += 1

        return self.data