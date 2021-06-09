import sys


def super_cat():
    try:
        name = [i for i in sys.argv if 'txt' in i][0] if 0 < len(
            sys.argv) < 6 else ''
        with open(name) as name:
            data = list(name.read().splitlines())
        data.sort() if '--sort' in sys.argv else data
        data = [f"{i} {e}" for i, e in enumerate(data)]\
            if '--num' in sys.argv else data
        data.append(
            f"rows count: {len(data)}") if "--count" in sys.argv else data
        return '\n'.join(data)
    except Exception:
        return 'ERROR'


if __name__ == '__main__':
    print(super_cat())
