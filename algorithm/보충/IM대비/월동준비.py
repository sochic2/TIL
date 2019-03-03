import sys
sys.stdin = open("월동준비.txt")

N = int(input())
data = list(map(int, input().split()))


mmax = max(data)
smart_sum = 0


for i in data:
    if i > 0:
        smart_sum += i


def dynamic_programming(meta):
    cache = [0] * len(meta)

    cache[0] = meta[0]

    for i in range(1, len(meta)):
        cache[i] = max(0, cache[i-1]) + meta[i]

    return max(cache)

print(dynamic_programming(data))

if smart_sum == 0:
    print(dynamic_programming(data), max(data))
else:
    print(dynamic_programming(data), smart_sum)



