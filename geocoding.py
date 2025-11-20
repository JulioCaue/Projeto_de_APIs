import requests

local=input('digite o cidade que quer ver a temperatura.')

# 1. URL de busca (Geocoding)
# Note que mudou de "api.open-meteo" para "geocoding-api.open-meteo"
url = ("https://geocoding-api.open-meteo.com/v1/search?name="+local)

# 2. Faz a chamada
resposta = requests.get(url)

dados_localização=resposta.json()
localização=dados_localização["'"+local+"'"]['latitude']['longitude']['elevation']
print (localização)

# 3. Mostra o resultado bruto
print(resposta.json())