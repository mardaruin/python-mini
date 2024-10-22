strs = [str(s) for s in input().split('|')]

def matrix(y):
  m = []
  for i in range(len(y)):
    m.append([float(s) for s in y[i].split()])
  return m

assert matrix("1 2 | 3 4".split('|')) == [[1.0, 2.0], [3.0, 4.0]]
assert matrix("34 64 34 | 45 28 5 | 3 78 9".split('|')) == [[34.0, 64.0, 34.0], [45.0, 28.0, 5.0], [3.0, 78.0, 9.0]]

print(matrix(strs))