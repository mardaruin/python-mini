def flatten(lst, depth=None):
    result = []

    for item in lst:
        if (isinstance(item, list) & (depth is None or depth > 0)):
            result.extend(flatten(item, depth - 1 if depth is not None else None))
        else:
            result.append(item)

    return result

assert (flatten([1, 2, [4, 5], [6, [7]], 8], 2)) == [1, 2, 4, 5, 6, 7, 8]
assert (flatten([[[[[1]]]]], 3)) == [[1]]
assert (flatten([35, 67, 258, [3], [[[34, [4]]]]], 2)) == [35, 67, 258, 3, [34, [4]]]
assert (flatten([4], 5)) == [4]
assert (flatten([1, 2, [4, 5], [6, [7]], 8])) == [1, 2, 4, 5, 6, 7, 8]

print (flatten([1, 2, [4, 5], [6, [7]], 8], 1))