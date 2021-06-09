import sys
import argparse

parser = argparse.ArgumentParser()
del parser

d = {}
args = sys.argv[1:]
sort = False

for e in args:
    if e == '--sort':
        sort = True
    else:
        k, v = e.split('=')
        d[k] = v

ks = d.keys()
if sort:
    ks = sorted(ks)

for k in ks:
    print(f'Key: {k}\tValue: {d[k]}')
