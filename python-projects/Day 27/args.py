# Positional arguments (unlimited)
# args is a tuple
def add(*args):
    print(type(args))
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(1,2,3,4,5))
print(add(1,2,3,4,5,6,7,8,9,10))


def calculate(n, **kwargs):
    # Keyword arguments (unlimited)
    # kwargs is a dictionary
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
    n += kwargs['add']
    n -= kwargs['sub']
    n *= kwargs['mul']
    n /= kwargs['div']
    return n


print(calculate(50, add=1, mul=2, div=3, sub=4))


class Car:
    def __init__(self, **kw):
        # get() function to get the value of the key in the dictionary, if the key is not in the dictionary,
        # it will return the default value, or it will return None if we don't specify the default value
        self.make = kw.get('make', 'Unknown')
        self.model = kw.get('model', 'Unknown')
        self.year = kw.get('year')


car1 = Car(make="Ford", model="Mustang", year=1964)




