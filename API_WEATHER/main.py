import requests


cities = ['Лондон', 'Череповец', 'Шереметьево']
request_params = {'m':'','M':'','lang':'ru'}

def get_weather(adress, params):
    response = requests.get(adress, params)
    response.raise_for_status()
    print(response.text)

for i in cities:
    url = f'http://wttr.in/{i}'
    get_weather(url, request_params)
