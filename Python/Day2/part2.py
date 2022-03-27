f = open('input.txt')

a = f.readlines()

S = 0

for i in range(len(a)):
    b = a[i].split("x")
    l = int(b[0])
    w = int(b[1])
    h = int(b[2])
    
    S += l * w * h + 2 * min(l + w, w + h, h + l)

f.close

f = open('output2.txt', 'w+')

print(str(S), file = f)

f.close
