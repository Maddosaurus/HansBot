from random import randrange
from pprint import pprint

import giphy_client
from giphy_client.rest import ApiException

from .settings import SETTINGS

api_instance = giphy_client.DefaultApi()

def searchme(term):
    try: 
    # Search Endpoint
        api_response = api_instance.gifs_search_get(SETTINGS.giphy_api_key, term, limit=50, offset=0, lang='en', fmt="json")
        random_number = randrange(len(api_response.data)-1)
        return api_response.data[random_number].url
    except ApiException as e:
        print("Exception while searching for GIF on giphy: %s\n" % e)
    
    return None

if __name__ == "__main__":
    searchme("flamethrower")