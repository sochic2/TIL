result = 1
c = 1
n = 153
a, b = 100, 200

while True:
    if n == 1: break

    if n % 2 == 0:
        n //= 2
        result += 1

    else:
        n = (n * 3) + 1
        result += 1
        if n < (b / 3) and c >= 1:
            n += 10
            c = c - 1
    print(n, end=' ')
print(result)