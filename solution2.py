a = [str(s) for s in input().split()]
b = [str(s) for s in input().split()]

def couples(x, y):
  c = []
  for i in range(min(len(x), len(y))):
    c.append ((x[i], y[i]))
  return c

assert couples([1, 2, 3], ["a", "b"]) == [(1, "a"), (2, "b")]
assert couples([1, 2, 0, 3, 4], ["wer", "asd"]) == [(1, "wer"), (2, "asd")]

print(couples(a, b))
