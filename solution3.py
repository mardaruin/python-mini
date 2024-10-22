strs = [str(s) for s in input().split('|')]

def matrix(y):
  m = []
  for i in range(len(y)):
    m.append([float(s) for s in y[i].split()])
  return m

assert matrix("1 2 | 3 4".split('|'))[0][1] == 2.0
assert matrix("34 64 34 | 45 28 5 | 3 78 9".split('|'))[2][2] == 9.0

print(matrix(strs)[0][1])