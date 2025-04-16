import requests

class ZipCodeAPI:
    def __init__(self):
        self.api_key = '0a73c740-1999-11f0-92dc-2f1ee961210b'
        self.base_url = 'https://app.zipcodebase.com/api/v1/code/city'

    def request_api_zipcode(self, city, state_name):
        """
        Get the zip code of given city and state.
        @param city string: The given city
        @param state_name string: The given state
        @return selected_zipcode string: The zip code given back from API query.
        """

        params = (
           ("apikey", self.api_key),
           ("city",city),
           ("state_name",state_name),
           ("country","us"),
        )

        response = requests.get(self.base_url, params=params)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return None
        else:
            zipcode_list = response.json()['results']
            return zipcode_list