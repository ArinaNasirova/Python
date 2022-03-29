LED = [[0]*1000 for i in range(1000)]

for i in range(1000):
    for j in range(1000):
        LED[i][j] = 0

def TurnOn(iMin, iMax, jMin, jMax: int):
    for i in range(iMin, iMax + 1):
        for j in range(jMin, jMax + 1):
            LED[i][j] += 1

def TurnOff(iMin, iMax, jMin, jMax: int):
    for i in range(iMin, iMax + 1):
        for j in range(jMin, jMax + 1):
            LED[i][j] -= 1
            if LED[i][j] < 0:
                LED[i][j] = 0

def Toggle(iMin, iMax, jMin, jMax: int):
    for i in range(iMin, iMax + 1):
        for j in range(jMin, jMax + 1):
            LED[i][j] += 2

f = open('input.txt')

S = f.readlines()

for i in range(len(S)):
    
    if S[i][0:4] == "turn":
        if S[i][5:7] == "on":
            for j in range(8, len(S[i])):
                if S[i][j + 1] == " ":
                    N = S[i][8:j + 1].split(",")
                    iMin = int(N[0])
                    jMin = int(N[1])
                    N = S[i][j + 10: len(S[i])].split(",")
                    iMax = int(N[0])
                    jMax = int(N[1])
                    TurnOn(iMin, iMax, jMin, jMax)
                    break
        else:
            for j in range(9, len(S[i])):
                if S[i][j + 1] == " ":
                    N = S[i][9:j + 1].split(",")
                    iMin = int(N[0])
                    jMin = int(N[1])
                    N = S[i][j + 10: len(S[i])].split(",")
                    iMax = int(N[0])
                    jMax = int(N[1])
                    TurnOff(iMin, iMax, jMin, jMax)
                    break
    else:
        for j in range(7, len(S[i])):
            if S[i][j + 1] == " ":
                N = S[i][7:j + 1].split(",")
                iMin = int(N[0])
                jMin = int(N[1])
                N = S[i][j + 10: len(S[i])].split(",")
                iMax = int(N[0])
                jMax = int(N[1])
                Toggle(iMin, iMax, jMin, jMax)
                break

f.close

CountLED = 0

for i in range(1000):
    for j in range(1000):
        CountLED += LED[i][j]

f = open('output2.txt', 'w+')

print(str(CountLED), file = f)

f.close
