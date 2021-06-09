import requests

geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Петровка+38&results=1&format=json"
response = requests.get(geocoder_request)

geo_info = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
print(geo_info['metaDataProperty']['GeocoderMetaData']['Address']['postal_code'])
