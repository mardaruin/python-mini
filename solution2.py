a = [str(s) for s in input().split()]
b = [str(s) for s in input().split()]

c = []

for i in range(min(len(a), len(b))):
    c.append ((str(a[i]), str(b[i])))

print(c)
