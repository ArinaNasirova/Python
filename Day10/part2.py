f = open('input.txt')

S = f.readline()

f.close

s =[""] * 51

s[0] = str(S)

for k in range(1, 51):

    i = 0
    
    while i < len(s[k - 1]):
        
        n = 1

        r = s[k - 1][i]
        
        for j in range(i + 1, len(s[k - 1]) - 1):
            q = s[k - 1][j]
            if r == q:
                n += 1
            else:
                break
        if i + n - 1 < len(s[k - 1]):
            s[k] += str(n) + r
        else:
            s[k] += str(n) + q

        i += 1 + n - 1

f = open('output2.txt', 'w+')

print(str(len(s[50])), file = f)

f.close
