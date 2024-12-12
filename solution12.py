from functools import wraps

def coroutine(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        coro = func(*args, **kwargs)
        next(coro)
        return coro
    return wrapper

@coroutine
def storage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)

st = storage()
print(st.send(42)) # False
print(st.send(42)) # True