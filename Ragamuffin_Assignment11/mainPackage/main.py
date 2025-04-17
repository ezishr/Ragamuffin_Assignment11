# File Name: write_to_csv.py
# Student Name: Eirlys Vo, Annapoorna Naire
# Email: vopq@mail.uc.edu, nairap@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date: April 17, 2025
# Course #/Section: IS 4010 - 001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Clean provided CSV data file in a way the code can work with similar data file.
# Brief Description of what this module does: Focus on working with data for assignment 11.
# Citations: N/A
# Anything else that's relevant: N/A

from CleanDataPackage.cleanData import *

if __name__ == "__main__":
    # Initialize the CleanData class with the CSV file link.
    clean = clean_full_data(csv_link = "Data/fuelPurchaseData.csv")

    # Invoke the clean_data method to clean the data.
    data = clean.clean_data()
    print("Data cleaned and saved to cleanedData.csv in Data folder.")