from dataclasses import dataclass

@dataclass
class Counter:
    count: int = 0
    step: int = 1

    def increment(self):
        self.count += self.step

class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def __init__(self, *args, **kwargs):
        super().__init__()

class GlobalCounter(Singleton, Counter):
    pass

gc1 = GlobalCounter()
gc2 = GlobalCounter()

assert id(gc1) == id(gc2)