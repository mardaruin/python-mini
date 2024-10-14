d = {"a": 97, "b": 55, "c": 67, "d": 55, "e": 12345}

swapped_dict = {value: tuple(key for key in d.keys() if value == d[key] ) for value in d.values()}

print(swapped_dict)