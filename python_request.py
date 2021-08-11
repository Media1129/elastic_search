# import requests

# headers = {
#     'Content-Type': 'application/json',
# }

# data = open('recipe_data.json', 'rb').read()
# response = requests.post('https://search-recipe-tnx35rcz5nydy2h2hry2qqqmvy.us-east-1.es.amazonaws.com/_bulk', headers=headers, data=data, auth=('Media1129', 'Miulab524$'))


import requests

params = (
    ('q', 'color:green'),
)

# response = requests.get('https://search-recipe-tnx35rcz5nydy2h2hry2qqqmvy.us-east-1.es.amazonaws.com/veggies2/_search', params=params, auth=('Media1129', 'Miulab524$'))
# print(response)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
response = requests.get('https://search-recipe-tnx35rcz5nydy2h2hry2qqqmvy.us-east-1.es.amazonaws.com/veggies/_search?q=color:green', auth=('Media1129', 'Miulab524$'))

print(response.status_code)
print(requests.codes.ok)
print(response.text)