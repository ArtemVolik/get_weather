import requests

cities = ['Лондон', 'Череповец', 'Шереметьево']
request_params = {'m': '', 'n':'', 'T':'', 'q':'', 'lang': 'ru'}


def get_weather(adress, params):
    response = requests.get(adress, params)
    response.raise_for_status()
    print(response.text)


def main():
    for city in cities:
        url = f'http://wttr.in/{city}'
        get_weather(url, request_params)


if __name__ == '__main__':
    main()
