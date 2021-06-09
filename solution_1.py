from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('arg', nargs='*')
    args = list(parser.parse_args().arg)

    if not args:
        print('NO PARAMS')
    elif len(args) < 2:
        print('TOO FEW PARAMS')
    elif len(args) == 2:
        try:
            print(sum(map(int, args)))
        except Exception as e:
            print(type(e).__name__)
    else:
        print('TOO MANY PARAMS')
