strs = [str(s) for s in input().split('|')]

matrix = []

for i in range(len(strs)):
    matrix.append([float(s) for s in strs[i].split()])

print(matrix)
print(matrix[0][1])