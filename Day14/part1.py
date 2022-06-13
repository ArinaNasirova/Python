f = open('input.txt')

S = f.readlines()

f.close()

velocity = []
time_move = []
time_relax = []

for i in range(len(S)):
    s = S[i].split()
    velocity.append(int(s[3]))
    time_move.append(int(s[6]))
    time_relax.append(int(s[13]))

R = []

for i in range(len(S)):

    n = int(2503 / (time_move[i] + time_relax[i]))
    
    l = n * velocity[i] * time_move[i]

    if 2503 - n * (time_move[i] + time_relax[i]) < time_move[i]:
        l += (2503 - n * (time_move[i] + time_relax[i])) * velocity[i]
    else:
        l += time_move[i] * velocity[i]
    
    
    R.append(int(l))

maxR = R[0]

for i in range(len(R)):
    if maxR < R[i]:
        maxR = R[i]

f = open('output1.txt', 'w+')

print(str(maxR), file = f)

f.close()
