import random

data = [random.randint(0, 101) for x in range(0, 10)]
print data

for i in range(0, len(data)):
    j = i + 1
    position = i
    min = data[i]
    while j < len(data):
        if data[j] < min:
            position = j
            min = data[j]
        j += 1
    tmp = data[i]
    data[i] = data[position]
    data[position] = tmp

print data