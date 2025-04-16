# File Name: readdata.py
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

class HelperFunction:
    def __init__(self, csv_link):
        self.csv_link = csv_link

    def read_CSV_file(self):
        '''
        Reads a particular CSV file into a list of lists.
        fuelPurchaseData.csv
        The first row is assumed to be a header and is skipped
        @return list: the list of lists that was created from the file
        '''
        csv_data = []
        with open(self.csv_link, newline='') as f:
            reader = csv.reader(f, delimiter=',')
            header = next(reader)
            for row in reader:
                csv_data.append(row)

        self.data = csv_data
        self.header = header

        return csv_data, header

    def delete_duplicates(self):
        """
        NOT DONE
        Delete duplicate rows
        @return: excel data without any duplicate rows 
        """
        #output_file = './Data/cleanedData.csv'

        unique_rows = []
        seen = set()

        for i in range(len(self.data) - 1):
            row = data[i].copy()
            print(f'index: {i}')
            #print(row)
            #row.pop(0)
            row_tuple = tuple(row)  
            if row_tuple not in seen:
                unique_rows.append(self.data[i])
                seen.add(row_tuple)
            print(f'seen len:{len(seen)}\nunique_rows len: {len(unique_rows)}')

        return seen, unique_rows

    def gross_price_two_decimals(self):
        """
        Make Gross Price column to have exactly 2 decimal places.
        @param data list: The converted CSV data to process.
        @return data list: The data after being processed.
        """

        gross_price_idx = self.header.index('Gross Price')

        for row in self.data:
            row[gross_price_idx] = f"{float(row[gross_price_idx]):.2f}"

        return self.data



    def detect_pepsi(self):
        """
        Delete rows having Fuel Type of Pepsi and write these rows into a CSV file named dataAnomalies.
        @param data list: The raw data to process.
        @param header list: Header of raw data.
        @return collected_row list: Data after being deleted with rows having Pepsi.
        """

        fuel_type_idx = self.header.index('Fuel Type')

        collected_row = [row for row in self.data if row[fuel_type_idx].strip().lower() != 'pepsi']
        anomalies_row = [row for row in self.data if row[fuel_type_idx].strip().lower() == 'pepsi']
        with open('Data/dataAnomalies.csv', mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(self.header)
            writer.writerows(anomalies_row)

        return collected_row