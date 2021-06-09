import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=argparse.FileType('r'))
    parser.add_argument('destination', type=argparse.FileType('w'))
    parser.add_argument('--upper', action='store_true')
    parser.add_argument('--lines', metavar='N', type=int, default=-1)
    args = parser.parse_args()

    if args.lines < 0:
        lines = args.source.readlines()
    else:
        lines = args.source.readlines()[:args.lines]
    res = ''.join(lines)
    if args.upper:
        res = res.upper()
    args.destination.write(res)
