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
def read_CSV_file(file_name):
    '''
    Reads a particular CSV file into a list of lists.
    fuelPurchaseData.csv
    The first row is assumed to be a header and is skipped
    @return list: the list of lists that was created from the file
    '''
    csv_data = []
    path = "./Data/" + file_name
    with open(f"./Data/{file_name}", newline='') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
        for row in reader:
            csv_data.append(row)
       
    return csv_data, header

"""
def two_decimals_only(raw_data, output_filename):
    Round Gross price to two decimal places
    @return: gross price so that it is properly rounded
    output_file = './Data/' + output_filename

    column_index = 2

    for i in range(len(data) - 1):
        try:
            data[i][column_index] = round(float(data[i][2]), 2)
        except ValueError:
            pass

        with open(output_file, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(data[i])

out = two_decimals_only(raw_data=data, output_filename='cleanedData.csv')
"""

def delete_duplicates(data):
    """
    NOT DONE
    Delete duplicate rows
    @return: excel data without any duplicate rows 
    """
    #output_file = './Data/cleanedData.csv'

    unique_rows = []
    seen = set()

    for i in range(len(data) - 1):
        row = data[i].copy()
        print(f'index: {i}')
        #print(row)
        #row.pop(0)
        row_tuple = tuple(row)  
        if row_tuple not in seen:
            unique_rows.append(data[i])
            seen.add(row_tuple)
        print(f'seen len:{len(seen)}\nunique_rows len: {len(unique_rows)}')

    return seen, unique_rows

def gross_price_two_decimals(data):
    """
    Make Gross Price column to have exactly 2 decimal places.
    @param data list: The converted CSV data to process.
    @return data list: The data after being processed.
    """

    for row in data:
        row[2] = f"{float(row[2]):.2f}"
    return data



def detect_pepsi(data, header):
    """
    Delete rows having Fuel Type of Pepsi and write these rows into a CSV file named dataAnomalies.
    @param data list: The raw data to process.
    @param header list: Header of raw data.
    @return collected_row list: Data after being deleted with rows having Pepsi.
    """

    collected_row = [row for row in data if row[5].strip().lower() != 'pepsi']
    anomalies_row = [row for row in data if row[5].strip().lower() == 'pepsi']
    with open('Data/dataAnomalies.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(header)
        writer.writerows(anomalies_row)

    return collected_row