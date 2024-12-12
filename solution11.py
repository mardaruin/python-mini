from itertools import islice

def cycle(iterable):
    saved = []
    for item in iterable:
        yield item
        saved.append(item)
    while True:
        yield from saved

def chain(*iterables):
    for it in iterables:
        yield from it


print(list(islice(cycle([1, 2, 3]), 10)))
print(list(chain([1, 2, 3], ['a', 'b'])))