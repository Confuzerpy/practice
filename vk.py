import datetime
import vk_api


def main():
    login, password = LOGIN, PASSWORD

    sess = vk_api.VkApi(login, password)

    try:
        sess.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        return error_msg

    vkont = sess.get_api()
    response = vkont.wall.get(count=5, offset=1)
    if response['items']:
        for i in response['items']:
            print(i['text'])
            x = str(datetime.datetime.fromtimestamp(i['date'])).split()
            print(f'date: {x[0]}, time: {x[1]}')


if __name__ == '__main__':
    main()
