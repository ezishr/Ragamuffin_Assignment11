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
#from curses import raw
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
        return csv_data


data = read_CSV_file(file_name = 'fuelPurchaseData.csv')
print(data[0])

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

def delete_duplicates(raw_data):
    """
    Delete duplicate rows
    @return: excel data without any duplicate rows 
    """
    output_file = './Data/cleanedData.csv'

    unique_rows = []
    seen = set()

    

    for i in range(len(raw_data) - 1):
        row = raw_data[i].copy()
        row.pop(0)
        row_tuple = tuple(row)  
        if row_tuple not in seen:
            unique_rows.append(raw_data[i])
            seen.add(row_tuple)

    return seen, unique_rows

seen, unique_rows = delete_duplicates(raw_data = data)
print(f'seen len: {len(seen)}\n unique len: {len(unique_rows)}')
