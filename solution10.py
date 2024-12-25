from dataclasses import dataclass

@dataclass
class Counter:
    count: int = 0
    step: int = 1
    some: int = 2

    def increment(self):
        self.count += self.step

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Singleton:
    _instances = None

    def no_function(self, *args, **kwargs):
        print("in no_function")
        pass

    def __new__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super().__new__(cls)
            print("in __new__, instance created ")
        else:
            cls.__init__ = cls.no_function
            print("in __new__, will return cls._instances ")
        return cls._instances


    def __init__(self, *args, **kwargs):
        print("in __init__ ")
        pass

class GlobalCounter(Singleton, Counter):
    pass

print("create first GlobalCounter ")
gc1 = GlobalCounter()
print("create second GlobalCounter ")
gc2 = GlobalCounter()

assert id(gc1) == id(gc2)

gc1.increment()
assert gc2.count == 1