f = open('input.txt')

a = f.readlines()

S = 0

for i in range(len(a)):
    b = a[i].split("x")
    l = int(b[0])
    w = int(b[1])
    h = int(b[2])
    
    S += 2 * (l * w + w * h + h * l) + min(l * w, w * h, h * l)

f.close

f = open('output1.txt', 'w+')

print(str(S), file = f)

f.close
