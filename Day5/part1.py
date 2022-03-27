def FirstCondition(st: str) -> bool:
    n = 0
    for i in range(len(st)):
        if st[i] == "a" or st[i] == "e" or st[i] == "i" or st[i] == "o" or st[i] == "u":
            n += 1
    if n >= 3:
        return True
    else:
        return False

def SecondCondition(st: str) -> bool:
    C = False
    for i in range(1, len(st)):
        if st[i] == st[i - 1]:
            C = True
    return C

def ThirdCondition(st: str) -> bool:
    C = True
    for i in range(1, len(st)):
        if C and (st[i - 1] == "a" and st[i] == "b" or st[i - 1] == "c" and st[i] == "d" or st[i - 1] == "p" and st[i] == "q"  or st[i - 1] == "x" and st[i] == "y"):
            C = False
    return C


f = open('input.txt')

S = f.readlines()

f.close

NiceCount = 0

for i in range(len(S)):
    if FirstCondition(S[i]) and SecondCondition(S[i]) and ThirdCondition(S[i]):
        NiceCount += 1

f = open('output1.txt', 'w+')

print(str(NiceCount), file = f)

f.close
