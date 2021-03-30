import sys
import csv


string = sys.stdin.read().split('\n')
param = string[]
ship, sp_ship = [], []
ship.append(string[4::])
for i in ship:
    for j in i:
        sp_ship.append(j.split(';'))

with open(string[2], encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index > 10:
            break
        print(row)

