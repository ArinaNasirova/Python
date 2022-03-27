f = open('input.txt')

S = f.readline()

f.close

CountHouses = 0

XCoords = []
YCoords = []

x = 0
y = 0

XCoords.append(x)
YCoords.append(y)
      
for i in range(len(S)):

    if S[i] == ">":
        x += 1

    if S[i] == "<":
        x -= 1
    
    if S[i] == "^":
        y += 1

    if S[i] == "v":
        y -= 1

    XCoords.append(x)
    YCoords.append(y)
    
for i in range(len(XCoords)):
    
    NewHouse = True
    
    for j in range(i):
        if NewHouse and XCoords[i] == XCoords[j] and YCoords[i] == YCoords[j]:
            NewHouse = False
            break
    
    if NewHouse:
        CountHouses += 1

f = open('output1.txt', 'w+')

print(str(CountHouses), file = f)

f.close
