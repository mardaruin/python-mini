from solution6 import flatten

def test_flatten():
    assert (flatten([1, 2, [4, 5], [6, [7]], 8], 2)) == [1, 2, 4, 5, 6, 7, 8]
    assert (flatten([[[[[1]]]]], 3)) == [[1]]
    assert (flatten([35, 67, 258, [3], [[[34, [4]]]]], 2)) == [35, 67, 258, 3, [34, [4]]]
    assert (flatten([4], 5)) == [4]
    assert (flatten([1, 2, [4, 5], [6, [7]], 8])) == [1, 2, 4, 5, 6, 7, 8]