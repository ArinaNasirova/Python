f = open('input.txt')

n = int(f.readline())

a = []

for i in range(n):
    a.append(int(f.readline()))

b = f.readline().split()

f.close

f = open('output.txt', 'w+')

for i in range(len(b)):
    
    k = -1
    
    for j in range(len(a)):
        if int(b[i]) == a[j]:
            k = j
            
    print(str(k), file = f)

f.close
