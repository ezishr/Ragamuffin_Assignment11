from inspect import cleandoc
from helperfunctionPackage.helperFunction import *
from zip_codePackage.zip_code import *

HelperFunction = HelperFunction('Data/fuelPurchaseData.csv')
data, header = HelperFunction.read_CSV_file()
data = HelperFunction.gross_price_two_decimals()
data = HelperFunction.detect_pepsi()
data = HelperFunction.fix_address()
data = HelperFunction.delete_duplicates()