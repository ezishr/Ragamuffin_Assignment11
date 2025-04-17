# File Name: cleanData.py
# Student Name: Eirlys Vo
# Email: nairap@mail.uc.edu, vopq@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date: April 17, 2025
# Course #/Section: IS 4010 - 001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Clean provided CSV data file in a way the code can work with similar data file.
# Brief Description of what this module does: Focus on working with data for assignment 11.
# Citations: N/A
# Anything else that's relevant: N/A


from helperfunctionPackage.helperFunction import *
from zip_codePackage.zip_code import *
from WriteToCSVPackage.write_to_csv import *

class clean_full_data:
    def __init__(self, csv_link):
        self.csv_link = csv_link

    def clean_data(self):
        helperFunction = HelperFunction(self.csv_link)
        self.data, self.header =  helperFunction.read_CSV_file()
        self.data = helperFunction.gross_price_two_decimals()
        self.data = helperFunction.detect_pepsi()
        self.data = helperFunction.fix_address()
        self.data = helperFunction.delete_duplicates()
        
        to_csv = Write_To_CSV(path = 'Data/cleanedData.csv', data = self.data, header = self.header)
        to_csv.write_to_csv_path()
        return self.data