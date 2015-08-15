import random

data = [random.randint(0, 101) for y in range(0, 10)]
print data

for i in range(1, len(data)):
    j = i - 1
    temp = data[i]
    while j >= 0 and temp < data[j]:
        data[j+1] = data[j]
        j -= 1
    data[j+1] = temp

print data