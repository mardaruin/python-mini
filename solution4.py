dict = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}

def swapped(d):
    pre_swapped_dict = {value: tuple(key for key in d.keys() if value == d[key] ) for value in d.values()}
    swapped_dict = {}
    for i in pre_swapped_dict.items():
        val = i[1]
        if len(val) > 1:
            swapped_dict.update({i[0]: val})
        else:
            swapped_dict.update({i[0]: val[0]})
    return swapped_dict

assert swapped({"a": 97, "b": 55, "c": 67, "d": 55, "e": 12345}) == {97: 'a', 55: ('b', 'd'), 67: 'c', 12345: 'e'}

print(swapped(dict))