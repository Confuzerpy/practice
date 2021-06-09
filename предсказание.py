import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--barbie", type=int, default=50)
parser.add_argument("--cars", type=int, default=50)
parser.add_argument("--movie", choices=['melodrama', 'football', 'other'], type=str, default='other')
args = parser.parse_args()

if args.movie == 'melodrama':
    movie = 0
elif args.movie == 'football':
    movie = 100
else:
    movie = 50

if args.barbie > 100 or args.barbie < 0:
    args.barbie = 50

if args.cars > 100 or args.cars < 0:
    args.cars = 50

boys = int((100 - args.barbie + args.cars + movie) / 3)

print(f'boy: {boys}')
print(f'girl: {100 - boys}')
