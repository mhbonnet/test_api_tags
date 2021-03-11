# -*- coding: utf-8 -*-

# This file is intented to test the tags API directly, 
# by sending a POST request with JSON data to the web site.
# It returns JSON data, displayed in the console.

import requests
import json

a_title = "What about learning python and pip and html?"
a_body = "I've always wondered if it was interesting. Because I'm not sure about what we can do with it... Let's check! I know java and c++, but I still don't know pandas very well, and I'm just starting with API. For HTML I know the basics."

url = "https://tags-api.herokuapp.com/api/"
#url = "http://127.0.0.1:5000/api/"
headers = {'Content-type': 'application/json'}

dict = {'title': a_title, 'body': a_body}

print('\nThe API sends a post request to the site {} :\n{}'.format(url, dict))
response = requests.post(url, json=dict, headers=headers)

if response.status_code != 200:
    print('error : ', response)
else:
    print('\nHere is the answer:')
    print(response.text)