def add(a, b):
    total = a + b
    return total


sum = add(2, 3)
print(sum)
print(add(10, 30))


def adder(a, b):
    total = a + b
    print(total)

adder(10, 50)
print(adder(10, 50))

def summ(arg):
    x = 0
    for i in arg:
        x += i
    return x

out = summ([1, 2, 3])
print(out)

# summ([10, 20], [30, 50])

# default argument
def greetings(msg = 'Morning'):
    print(f'Good {msg}')
    print('Welcome to the function')

greetings()
greetings('Evening')