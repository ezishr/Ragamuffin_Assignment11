# File Name: cleanData.py
# Student Name: Eirlys Vo
# Email: vopq@mail.uc.edu
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
    """
    This class is responsible for cleaning the data from the CSV file.
    """

    def __init__(self, csv_link):
        """
        Initialize the class with the CSV file link.
        @param csv_link: The link to the CSV file.
        """
        self.csv_link = csv_link

    def clean_data(self):
        """
        This method cleans the data by reading the CSV file, processing it, and writing the cleaned data to a new CSV file.
        """
        helperFunction = HelperFunction(self.csv_link) # Initialize the helper function class.
        self.data, self.header =  helperFunction.read_CSV_file() # Read the data and header from the CSV file.
        self.data = helperFunction.gross_price_two_decimals() # Round the gross price to two decimal places.
        self.data = helperFunction.detect_pepsi() # Detect if the brand is Pepsi.
        self.data = helperFunction.fix_address() # Add zip code to address that misses it.
        self.data = helperFunction.delete_duplicates() # Delete duplicates from the data.
        
        to_csv = Write_To_CSV(path = 'Data/cleanedData.csv', data = self.data, header = self.header) # Initialize the Write_To_CSV class.
        to_csv.write_to_csv_path() # Write the cleaned data to a new CSV file.
        return self.data