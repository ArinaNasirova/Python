f = open('input.txt')

S = f.read()

f.close()

with open('input.txt', 'r') as f:
    items = f.read()

totalsec = 2503
score = dict()
dist = dict()
stats = []

for S in S.split('\n'):
    n, _, _, speed, _, _, ftime,  _, _, _, _, _, _, rtime, _ = S.split(" ")
    stats.append((n, int(speed), int(ftime), int(rtime)))
    dist[n] = 0
    score[n] = 0

for i in range(totalsec):
    for n, speed, ftime, rtime in stats:
        if i % (ftime + rtime) < ftime:
            dist[n] += speed

    best = max(dist.values())
    for n, d in dist.items():
        if d == best:
            score[n] += 1

f = open('output2.txt', 'w+')

print(max(score.values()), file = f)

f.close()
