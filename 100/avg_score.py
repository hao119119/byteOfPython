import random
score = []
for i in range(0, 10):
    score.append(random.randint(0, 101))
print score

total = 0
minN = maxN = score[0]
for i in range(0, 10):
    if maxN < score[i]:
        maxN = score[i]
    if minN > score[i]:
        minN = score[i]
    total += score[i]

print minN
print maxN

total = total - maxN - minN
avg = total/8
print avg

