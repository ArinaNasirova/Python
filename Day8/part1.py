N = 0

K = 0

f = open('input.txt')

S = f.readlines()

f.close

for j in range(len(S)):
    
    N += len(S[j]) - 1

    i = 1

    while (i < len(S[j]) - 2):

        K += 1
        
        if S[j][i] == "\\" and i + 1 < len(S[j]) - 1:

            if S[j][i + 1] == "\"" or S[j][i + 1] == "\\":
                i += 1
            elif S[j][i + 1] == "x" and i + 3 < len(S[j]) - 1:
                fn = S[j][i + 2].isdigit() or S[j][i + 2] == "a" or S[j][i + 2] == "b" or S[j][i + 2] == "c" or S[j][i + 2] == "d" or S[j][i + 2] == "e" or S[j][i + 2] == "f"
                sn = S[j][i + 3].isdigit() or S[j][i + 3] == "a" or S[j][i + 3] == "b" or S[j][i + 3] == "c" or S[j][i + 3] == "d" or S[j][i + 3] == "e" or S[j][i + 3] == "f"
                if fn and sn:
                    i += 3
        
        i += 1

f = open('output1.txt', 'w+')

print(str(N - K), file = f)

f.close
