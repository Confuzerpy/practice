import sqlite3

bd, first, second, third = input(), input().split(), input().split(), input().split()

con = sqlite3.connect(bd)
cur = con.cursor()
result = cur.execute("""SELECT * FROM towage
                        WHERE ? ? ? AND ? ? ?""", (first[0], first[1],
                        first[2], second[0], second[1], second[2], 
                        )).fetchall()
team = []

for i in result:
    print(i)
    # for j in i:
        # team.append(j)

con.close()
