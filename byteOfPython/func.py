x = 50


def func(x):
    print 'x is ', x
    x = 2
    print 'change local x to', x

func(x)
print 'x is still', x


# global value
def func_a():
    global x
    print 'x is ', x
    x = 2
    print 'Changed global x to ', x

func_a()
print 'value of x is', x


# default argument values
def say(message, times=1):
    print message * times

say('hello')
say('world', 5)


def func_b(a, b=5, c=10):
    print 'a is', a, 'and b is', b, 'and c is', c

func_b(3, 7)
func_b(25, c=24)
func_b(c=50, a=100)


def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print total(10, 1, 2, 3, vegetables=50, fruits=100)


def print_max(z, y):
    '''Prints the maximum of two numbers.

    the two values must be integers.'''
    # convert to integers, if possible
    z = int(z)
    y = int(y)

    if z > y:
        print z, 'is maximum'
    else:
        print y, 'is maximum'

print_max(3, 6)
print print_max.__doc__
