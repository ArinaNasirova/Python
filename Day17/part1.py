from itertools import combinations

volumes = []

with open('input.txt','r') as INPUT:
    for line in INPUT:
        line = line.strip()
        volumes.append(line)
liters = 150

sum_array = []
for i in range(1,len(volumes)):
    array = list(combinations(volumes, i+1))
    summa = 0
    for element in array:
        for j in range(len(element)):
            summa += int(element[j])
        if summa == liters:
            sum_array.append(element)
        summa = 0

with open('output1.txt','w') as OUTPUT:
    OUTPUT.write(str(len(sum_array)))
