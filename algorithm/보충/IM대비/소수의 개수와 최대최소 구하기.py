import sys
sys.stdin = open('소수.txt')
a, b = map(int, input().split())


def check_sosu(n):
    sosu = [0, 0] + [1] * (n-1)
    for i in range(int(len(sosu)**0.5)+1):
        if sosu[i] != 0:
            k = i * 2
            while k <= n:
                sosu[k] = 0
                k += i
    return [i for i in range(len(sosu)) if sosu[i]]

result_data = check_sosu(b)

final_data = []
for k in result_data:
    if k >= a:
        final_data.append(k)


print(len(final_data))
print(max(final_data)+min(final_data))




