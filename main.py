#define função de pegar clima
def get_clima(cidade):

    import requests
    # 1. Montar URL de Geocoding usando 'cidade'
    Localizador = (f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}")
    # 2. Fazer request e pegar lat/lon
    Dados_Localização = requests.get(Localizador)
    dados=Dados_Localização.json()
    try:
        lat=dados['results'][0]['latitude']
        lon=dados['results'][0]['longitude']
    # 3. Montar URL de Clima
        Pegar_Temperatura = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    # 4. Fazer request e pegar temperatura
        resposta = requests.get(Pegar_Temperatura)
    # 5. return temperatura
        if resposta.status_code == 200:
            dados=resposta.json()
            temperatura=dados['current_weather']['temperature']
            return temperatura
            
        else:
            return None
    except:
        return None
#Logica de input/output
while True:
    cidade=input('Digite o nome da ciadade ou digite sair: ')
    if cidade==('sair'):
        break

    temperatura=get_clima(cidade)
    #Se não for none, deu certo
    if temperatura is not None:
        print (f'A temperatura atual em {cidade.capitalize()} é {temperatura}°C')
    #se for none, deu ruim.
    else:
        print("Cidade não encontrada. Tente de novo.")