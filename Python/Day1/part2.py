f = open('input.txt')

S = f.readline()

f.close

floor = 0

first_basement_position = 0

for i in range(len(S)):
    
    floor = floor + 1 if S[i] == "(" else floor - 1
    
    if floor < 0:
        first_basement_position = i + 1
        break

f = open('output2.txt', 'w+')

print(str(first_basement_position), file = f)

f.close
