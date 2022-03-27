f = open('input.txt')

S = f.readline()

f.close

CountHouses = 0

XCoords = []
YCoords = []

XCoords1 = []
YCoords1 = []

x0 = 0
y0 = 0

x1 = 0
y1 = 0

XCoords.append(int(0))
YCoords.append(int(0))
      
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == ">":
            x0 += 1

        if S[i] == "<":
            x0 -= 1
        
        if S[i] == "^":
            y0 += 1

        if S[i] == "v":
            y0 -= 1

        XCoords.append(x0)
        YCoords.append(y0)

    if i % 2 == 1:
        if S[i] == ">":
            x1 += 1

        if S[i] == "<":
            x1 -= 1
        
        if S[i] == "^":
            y1 += 1

        if S[i] == "v":
            y1 -= 1

        XCoords.append(x1)
        YCoords.append(y1)
    
for i in range(len(XCoords)):
    
    NewHouse = True
    
    for j in range(i):
        if NewHouse and XCoords[i] == XCoords[j] and YCoords[i] == YCoords[j]:
            NewHouse = False
            break
    
    if NewHouse:
        CountHouses += 1

f = open('output2.txt', 'w+')

print(str(CountHouses), file = f)

f.close
