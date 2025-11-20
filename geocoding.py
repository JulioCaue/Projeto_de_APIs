import requests

local=input('digite o cidade que quer ver a temperatura.')

# 1. URL de busca (Geocoding)
# Note que mudou de "api.open-meteo" para "geocoding-api.open-meteo"
Localizador = ("https://geocoding-api.open-meteo.com/v1/search?name="+local)

# 2. Faz a chamada
Dados_Localização = requests.get(Localizador)

dados=Dados_Localização.json()
lat=dados['results'][0]['latitude']
lon=dados['results'][0]['longitude']
# 3. Mostra o resultado bruto
#print(resposta.json())