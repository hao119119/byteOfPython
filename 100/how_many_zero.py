N = 100
total = 1
for i in range(1, N+1):
    total *= i

my_str = str(total)
print my_str


i = 0
for x in my_str[-1:0:-1]:
    if x == '0':
        i += 1
    else:
        break
print i
