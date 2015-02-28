shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# indexing or 'Subscription' operation
print 'Item 0 is', shoplist[0]
print 'Item 1 is', shoplist[1]
print 'Item 2 is', shoplist[2]
print 'Item 3 is', shoplist[3]
print 'Item -1 is', shoplist[-1]
print 'Item -2 is', shoplist[-2]

print 'Character 0 is', name[0]

# slicing on a list
print 'Item 1 to 3 is', shoplist[1:3]
print 'Item 2 to end is', shoplist[2:]
print 'Item 1 to -1 is', shoplist[1:-1]
print 'Item start to end is', shoplist[:]

# slicing on a string
print 'characters 1 to 3 is', name[1:3]
print 'characters 2 to end is', name[2:]
print 'characters 1 to -1 is', name[1:-1]
print 'characters start to end is', name[:]

# You can also provide a third argument for the slice, which is the step for the slicing
# (by default, the step size is 1):
print shoplist[::1]
print shoplist[::2]
print shoplist[::3]
