#!/usr/local/bin/python3

import json
import requests

url = 'https://api.chucknorris.io/jokes/random'
""" Example Chuck Norris response:
    {
    "categories": [],
    "created_at": "2020-01-05 13:42:21.455187",
    "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
    "id": "LmDiUYrLRmWERMIyqPIHSA",
    "updated_at": "2020-01-05 13:42:21.455187",
    "url": "https://api.chucknorris.io/jokes/LmDiUYrLRmWERMIyqPIHSA",
    "value": "Chuck Norris uses two 11 yr old kids and a scarf as his nunchucks."
    }
"""
    

def get_chuck_joke(api):
    """
    Get a random joke from the Chuck Norris API and return the serial JSON
    :param api:
    :return:serial JSON
    """
    #response = #  TASK 1 - use requests to get a joke.
    # Get random joke from using the global varialbe url
    response = requests.get(api)

    #return #  TASK 2 - return the response in JSON format
    #print(response.text)
    return json.loads(response.text)


if __name__ == '__main__':
    #  TASK 3 - correct the json statement
    joke = get_chuck_joke(url) 
    
    #  TASK 4 - print just a joke without any superfluous symbols
    print(joke['value']) 
