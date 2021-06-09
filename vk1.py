import vk_api


def main():
    lst = []
    login, password = LOGIN, PASSWORD
    sess = vk_api.VkApi(login, password)
    try:
        sess.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        return error_msg

    vkont = sess.get_api()
    response = vkont.friends.get(fields="bdate, city")

    if response['items']:
        for i in response['items']:
            try:
                lst.append([i['last_name'], i['first_name'], i['bdate']])
            except KeyError:
                pass
            lst = sorted(lst, key=lambda x: x[0])
        print('\n'.join([' '.join(i) for i in lst]))


if __name__ == '__main__':
    main()
