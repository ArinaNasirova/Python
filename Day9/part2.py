from itertools import permutations

def Distance(st0, st1: str) -> int:
    for i in range(len(S)):
        if st0 == gates[0][i] and st1 == gates[1][i] or st1 == gates[0][i] and st0 == gates[1][i]:
            return int(gates[2][i])

f = open('input.txt')

S = f.readlines()

f.close

gates = [[''] * len(S) for i in range(3)]

for i in range(len(S)):
    r = S[i].split()
    gates[0][i] = r[0]
    gates[1][i] = r[2]
    gates[2][i] = r[4]

places = []

for i in gates[0]:
    if i not in places:
        places.append(i)

for i in gates[1]:
    if i not in places:
        places.append(i)

CountPlaces = 1
for i in range(len(places)):
    CountPlaces *= i + 1

ls = []
for i in range(len(places)):
    ls.append(i)

for p in permutations(ls):
    lines = p

lines = list(permutations(ls))

Dists = [0] * CountPlaces

for i in range(CountPlaces):

    d = 0

    for j in range(1, len(places)):
        d += Distance(places[lines[i][j - 1]], places[lines[i][j]])

    Dists[i] = d

maxD = Dists[0]

for i in range(1, CountPlaces):
    if Dists[i] > maxD:
        maxD = Dists[i]

f = open('output2.txt', 'w+')

print(str(maxD), file = f)

f.close
