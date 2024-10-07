a = int(input())
count = 0
numberofbits = 1

if a > 0:
    while a > 0:
        count += a % 2
        a //= 2
else:
    a *= -1
    count = 1
    if a % 2 == 0:
        while a % 2 == 0:
            numberofbits += 1
            a //= 2
        count += 1
    else: count += 1
    while a > 0:
        numberofbits += 1
        count += (a + 1) % 2
        a //= 2
    if numberofbits % 8 != 0:
        count += 8 - numberofbits % 8


print(count)
