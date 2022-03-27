f = open('input.txt')

S = f.readline()

f.close

floor = 0

for i in range(len(S)):
    floor = floor + 1 if S[i] == "(" else floor - 1

f = open('output1.txt', 'w+')

print(str(floor), file = f)

f.close
