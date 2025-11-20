import requests

local=input('digite o cidade que quer ver a temperatura: ')
Localizador = (f"https://geocoding-api.open-meteo.com/v1/search?name={local}")

Dados_Localização = requests.get(Localizador)

dados=Dados_Localização.json()
lat=dados['results'][0]['latitude']
lon=dados['results'][0]['longitude']

# 1. Definir para onde vamos ligar (URL)
Pegar_Temperatura = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

# 2. Fazer a chamada (GET)
resposta = requests.get(Pegar_Temperatura)

# 3. Ver se funcionou (200 = OK)
if resposta.status_code == 200:
    print("Conexão bem sucedida!")
    print("Dados recebidos:")
    dados=resposta.json()
    temperatura=dados['current_weather']['temperature']
    print (f'A temperatura atual em {local.capitalize()} é {temperatura}°C')
    
else:
    print("Deu erro na conexão:", resposta.status_code)