import requests 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '24a7651b99f348a8256dfebd25625f29'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "badenoko@ya.ru",
    "password": "01urik"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Глюк",
    "photo_id": -1
}

'''response = requests.post(url= f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.json)'''

'''response_confirmation = requests.post(url= f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.json)'''

response_create = requests.post(url= f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.json)

message = response_create.json()['message']
print(message)
id = response_create.json()['id']
print(id)

{
 "pokemon_id" : id   
}

body_create = {
    "pokemon_id" : id,
    "name": "Лом",
    "photo_id": 55
}

response_create = requests.put(url= f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.json)

response_create = requests.post(url= f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_create)
print(response_create.json)