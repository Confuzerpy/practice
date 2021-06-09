import requests


def find_region(city):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={city}, 1&format=json"

    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()

        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][1]["name"]
        print(city, "относится к федеральному округу:", toponym_address)
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")



for city in ['Хабаровск', 'Уфа', 'Нижний Новгород', 'Калининград']:
    find_region(city)
