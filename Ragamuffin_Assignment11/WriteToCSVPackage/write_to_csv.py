# File Name: write_to_csv.py
# Student Name: Eirlys Vo
# Email: vopq@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date: April 17, 2025
# Course #/Section: IS 4010 - 001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Clean provided CSV data file in a way the code can work with similar data file.
# Brief Description of what this module does: Focus on working with data for assignment 11.
# Citations: https://docs.python.org/3/library/csv.html
# Anything else that's relevant: N/A

import csv

class Write_To_CSV:
    """
    This class is used to write data to a CSV file.
    """
    def __init__(self, path, data, header):
        """
        Initialize the Write_To_CSV class with the path, data, and header.
        @param path string: The path to the CSV file.
        @param data list: The data to be written to the CSV file.
        @param header list: The header of the CSV file.
        """
        self.path = path
        self.data = data
        self.header = header

    def write_to_csv_path(self):
        """
        Write the data to the CSV file at the specified path.
        """
        with open(self.path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(self.header)
            writer.writerows(self.data)