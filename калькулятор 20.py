import sys

try:
    lst_first = sys.argv[1::]
    if not lst_first:
        print('NO PARAMS')
        sys.exit()
    lst = []
    for i in lst_first:
        if int(i):
            lst.append(int(i))
        elif int(i.lstrip('0')):
            lst.append(int(i))
    lst = list(map(lambda x: x * (-1) if lst.index(x) % 2 else x, lst))
    print(sum(lst))
except Exception as ex:
    print(type(ex).__name__)