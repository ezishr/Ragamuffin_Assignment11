from CleanDataPackage.cleanData import *

if __name__ == "__main__":
    clean = clean_full_data(csv_link = "Data/fuelPurchaseData.csv")
    data = clean.clean_data()
    print(data[0])

