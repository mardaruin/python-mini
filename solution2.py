a = [str(s) for s in input().split()]
b = [str(s) for s in input().split()]

#y = [1, 3, 5, 7, 9, 11, 13453, 24435]
#x = [0, 2, 4, 6, 8, 10]

c = []

for i in range(min(len(a), len(b))):
    c.append ((str(a[i]), str(b[i])))

print(c)
