f = open('input.txt')

n = int(f.readline())

a = []

for i in range(n):
    a.append(f.readline())

f.close

#for i in range(n):
#    print(a[i])

f = open('output.txt', 'w+')

for i in range(n):

    x = 0
    
    for j in range(len(a[i]) - 1):
        
        if a[i][int(len(a[i])) - 2 - j] == 'F':
            x += 15 * 16 ** j
        elif a[i][int(len(a[i])) - 2 - j] == 'E':
            x += 14 * 16 ** j
        elif a[i][int(len(a[i])) - 2 - j] == 'D':
            x += 13 * 16 ** j
        elif a[i][int(len(a[i])) - 2 - j] == 'C':
            x += 12 * 16 ** j
        elif a[i][int(len(a[i])) - 2 - j] == 'B':
            x += 11 * 16 ** j
        elif a[i][int(len(a[i])) - 2 - j] == 'A':
            x += 10 * 16 ** j
        else:
            x += int(a[i][int(len(a[i])) - 2 - j]) * 16 ** j

    print(str(x), file = f)

f.close
