import requests
API_ZIP_CODE = '0a73c740-1999-11f0-92dc-2f1ee961210b'

def request_api_zipcode(city, state_name):
    """
    Get the zip code of given city and state.
    @param city string: The given city
    @param state_name string: The given state
    @return selected_zipcode string: The zip code given back from API query.
    """

    params = (
       ("apikey", API_ZIP_CODE),
       ("city",city),
       ("state_name",state_name),
       ("country","us"),
    );

    response = requests.get('https://app.zipcodebase.com/api/v1/code/city', params=params)
    print(response)
    print('\n')
    selected_zipcode = response.json()['results'][0]

    return selected_zipcode