import requests

API_URL = "https://restcountries.com/v3.1/all"

def get_country_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        countries = []
        for country_data in data:
            country = {
                "name": country_data["name"]["common"],
                "capital": country_data["capital"][0] if "capital" in country_data else None,
                "currency": list(country_data["currencies"].values())[0]["name"] if "currencies" in country_data else None,
                "continent": country_data["region"],
                # Grab just the first language of the list, in the future we can grab all languages
                "language": list(country_data["languages"].values())[0] if "languages" in country_data else None,
                "population": country_data["population"],
                "flag": country_data["flags"]["png"] if "flags" in country_data else None,
            }
            countries.append(country)
        return countries
    else:
        raise Exception('Failed getting country data')
