import requests
import json

token = '27b61d3224c2acc758918f3fae210b3d'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    
    "name": "Пузозаврик",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})
print(response.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 1350,
    "name": " ",
    "photo": ""
})
print(response_put.text)

response_post = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token' : token}, json={
    "pokemon_id": "1350"
})
print(response_post.text)