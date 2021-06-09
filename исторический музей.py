import requests

geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Красная площадь+1&results=1&format=json"
response = requests.get(geocoder_request)

geo_info = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
coords = geo_info['Point']['pos']
adress = geo_info['metaDataProperty']['GeocoderMetaData']['text']

print(f'Адрес Исторического музея города Москвы - {adress};')
print(f'Имеет координаты - {coords}.')
