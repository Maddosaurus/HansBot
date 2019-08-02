from random import randrange
from pprint import pprint

import giphy_client
from giphy_client.rest import ApiException

api_instance = giphy_client.DefaultApi()
api_key = 'm8YJUbFcMaX2YNMQOCPiesVmGMf6Xq5U' # str | Giphy API Key.
term = 'cheeseburgers' # str | Search query term or prhase.
limit = 50 # int | The maximum number of records to return. (optional) (default to 25)
offset = 0 # int | An optional results offset. Defaults to 0. (optional) (default to 0)
rating = 'g' # str | Filters results by specified rating. (optional)
lang = 'en' # str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)


def searchme(term):
    try: 
    # Search Endpoint
        api_response = api_instance.gifs_search_get(api_key, term, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)
        random_number = randrange(len(api_response.data)-1)
        return api_response.data[random_number].url
    except ApiException as e:
        print("Exception while searching for GIF on giphy: %s\n" % e)
    
    return None

if __name__ == "__main__":
    searchme("flamethrower")