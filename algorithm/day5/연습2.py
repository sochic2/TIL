# 나
def itoa(a):
    if a > 0:
        result = []
        i = 10
        while a != 0:
            result += [chr(a % i + ord('0'))]
            a //= 10
    result.reverse()
    result = "".join(result)
    return result

x = 123
print(x, type(x))
str1 = itoa(x)
print(str1, type(str1))



# 강사님
def itoa(x):
    str = list()

    y = 0
    while True:
        y = x % 10
        str.append(chr(y + ord('0')))
        x //= 10
        if x == 0:
            break

    str.reverse()
    str = "".join(str)
    return str

x = 123
print(x, type(x))
str1 = itoa(x)
print(str1, type(str1))