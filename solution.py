a = int(input())
count = 0

if a < 0:
    count += 1
    a *= -1
while a > 0:
    count += a%2
    a = a // 2

print(count)
