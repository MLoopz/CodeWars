class LazyInit(type):
    def __new__(cls, name, bases, attrs):
        nw = super(LazyInit, cls).__new__(cls, name, bases, attrs)

        def __init__(self, *args):
            for k, v in zip(attrs['__init__'].__code__.co_varnames[1:], args):
                setattr(self, k, v)
        setattr(nw, '__init__', __init__)
        return nw


class Person(metaclass=LazyInit):
    def __init__(self, name, age): 
        pass

class Circle(metaclass=LazyInit):
    def __init__(self, x, ray): 
        pass



a_person = Person('Luke', 21)
a_circle = Circle(1,5)

print(a_person.name == 'Luke')# 'Ehi, my name is Luke')
print(a_person.age == 21)# 'Ehi my age is 21')
print(a_circle.x == 1)# 'x is 1')
print(a_circle.ray == 5)# 'ray is 5')