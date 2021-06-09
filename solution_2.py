import sys
import argparse

if __name__ == '__main__':
    args = sys.argv[1:]
    parser = argparse.ArgumentParser()
    del parser
    c, n, s = False, False, False
    if args:
        if '--count' in args:
            c = True
            args.remove('--count')
        if '--num' in args:
            n = True
            args.remove('--num')
        if '--sort' in args:
            s = True
            args.remove('--sort')
        if len(args) == 1:
            try:
                with open(args[0]) as f:
                    lines = f.read().split('\n')
                    if s:
                        lines.sort()
                    for i, line in enumerate(lines):
                        if n:
                            print(i, line)
                        else:
                            print(line)
                    if c:
                        print('rows count:', len(lines))
                    exit(0)
            except Exception:
                pass

    print('ERROR')
