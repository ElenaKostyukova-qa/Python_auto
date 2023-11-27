import requests

response = requests.post(
    url='https://api.pokemonbattle.me:9104/pokemons',
    json={
        "name": "Мурзилка",
        "photo": "https://dolnikov.ru/pokemons/albums/001.png"
        },
    headers={
        'Content-Type': 'application/json',
        'trainer_token': '1c5724a00ff02f16d8eeec19afae21db'
        })

print(response.text)

response = requests.put(
    url='https://api.pokemonbattle.me:9104/pokemons',
    json={
        "pokemon_id": "20657",
        "name": "Крокодил",
        "photo": "https://dolnikov.ru/pokemons/albums/001.png"
        },
    headers={
        'Content-Type': 'application/json',
        'trainer_token': '1c5724a00ff02f16d8eeec19afae21db'
        })

print(response.text)



response = requests.post(
    url='https://api.pokemonbattle.me:9104/trainers/add_pokeball',
    json={
        "pokemon_id": "20657",
        },
    headers={
        'Content-Type': 'application/json',
        'trainer_token': '1c5724a00ff02f16d8eeec19afae21db'
        })

print(response.text)

