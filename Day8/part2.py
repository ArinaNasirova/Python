K = 0

f = open('input.txt')

S = f.readlines()

f.close

for j in range(len(S)):

    i = 1

    K += 4
    
    while (i < len(S[j]) - 2):

        if S[j][i] == "\\":
            K += 1

        if S[j][i] == "\"":
            K += 1
        
        i += 1

f = open('output2.txt', 'w+')

print(str(K), file = f)

f.close
