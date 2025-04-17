# File Name: zip_code.py
# Student Name: Eirlys Vo
# Email: vopq@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date: April 17, 2025
# Course #/Section: IS 4010 - 001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Clean provided CSV data file in a way the code can work with similar data file.
# Brief Description of what this module does: Focus on working with data for assignment 11.
# Citations: https://app.zipcodebase.com/documentation
# Anything else that's relevant: N/A

import requests

class ZipCodeAPI:
    """
    Zip Code API class to request the API and get zip code based on given city and state.
    """

    def __init__(self):
        """
        Initialize class with attributes api_key and base_url.
        """

        # Store the API key in api_key and base URL in base_url attributes.
        self.api_key = '0a73c740-1999-11f0-92dc-2f1ee961210b'
        self.base_url = 'https://app.zipcodebase.com/api/v1/code/city'

    def request_api_zipcode(self, city, state_name):
        """
        Get the zip code of given city and state.
        @param city string: The given city
        @param state_name string: The given state
        @return zipcode_list String or None: List of zip code from request if there is, otherwise None.
        """

        # Required params from Zip Code Base API documentation in order to get the zip code based on provided city and state name.
        params = (
           ("apikey", self.api_key),
           ("city",city),
           ("state_name",state_name),
           ("country","us"),
        )

        # Make the API request and store back to response variable.
        response = requests.get(self.base_url, params=params)

        # Check if the API request is made successfully (code error is 200).
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return None
        else:
            # If the request is success, store every found zip code as a list to zipcode_list and return this list.
            zipcode_list = response.json()['results']
            return zipcode_list