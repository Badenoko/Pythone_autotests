import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '24a7651b99f348a8256dfebd25625f29'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '33623'

def test_get_trainers():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200


def test_get_trainer_id():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200