from dataclasses import dataclass

@dataclass
class Counter:
    count: int = 0
    step: int = 1

    def increment(self):
        self.count += self.step

class Singleton:
    _instances = None

    def __new__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super().__new__(cls)
            cls._instances.__init__(*args, **kwargs)
        return cls._instances

    def __init__(self, *args, **kwargs):
        pass

class GlobalCounter(Singleton, Counter):
    pass

gc1 = GlobalCounter()
gc2 = GlobalCounter()

assert id(gc1) == id(gc2)