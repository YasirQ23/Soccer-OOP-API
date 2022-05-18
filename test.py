from pip._vendor import requests as r

request = r.get('https://foxes90-prempundit.herokuapp.com/players')
players_api = request.json()
print(players_api['Players'][0]['first_name'])


