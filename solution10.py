from dataclasses import dataclass

@dataclass
class Counter:
    count: int = 0
    step: int = 1

    def increment(self):
        self.count += self.step

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

class GlobalCounter(Singleton, Counter):
    pass

gc1 = GlobalCounter()
gc2 = GlobalCounter()

assert id(gc1) == id(gc2)