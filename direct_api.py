# -*- coding: utf-8 -*-

import requests

a_title = "What about learning python and pip and html?"
a_body = "I've always wondered if it was interesting. Because I'm not sure about what we can do with it... Let's check! I know java and c++, but I still don't know pandas very well, and I'm just starting with API. For HTML I know the basics."

url = "https://tags-api.herokuapp.com/api/"

dic = {
    'title': a_title,
    'body': a_body
}
print('The API sends a post request to the site...\n', dic)
response = requests.post(url, data = dic)

print('\nHere is the answer:')
print(response.text)