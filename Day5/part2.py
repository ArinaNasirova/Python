def FirstCondition(st: str) -> bool:
    C = False
    for i in range(len(st) - 1):
        for j in range(i + 2, len(st) - 1):
            if st[i] == st[j] and st[i + 1] == st[j + 1]:
                C= True
    return C

def SecondCondition(st: str) -> bool:
    C = False
    for i in range(len(st) - 2):
        if st[i] == st[i + 2]:
            C = True
    return C


f = open('input.txt')

S = f.readlines()

f.close

NiceCount = 0

for i in range(len(S)):
    if FirstCondition(S[i]) and SecondCondition(S[i]):
        NiceCount += 1

f = open('output2.txt', 'w+')

print(str(NiceCount), file = f)

f.close
