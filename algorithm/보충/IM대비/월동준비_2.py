import sys
sys.stdin = open("월동준비.txt")

N = int(input())
data = list(map(int, input().split()))




smart_sum = 0
mmax = -12345
stupid_sum = 0

for i in range(len(data)):
    if data[i] > 0:
        smart_sum += data[i]
    if stupid_sum + data[i] < data[i]:
        stupid_sum = data[i]
        if mmax < stupid_sum:
            mmax = stupid_sum
    else:
        stupid_sum += data[i]
        if mmax < stupid_sum:
            mmax = stupid_sum


if smart_sum == 0:
    smart_sum = max(data)

print(mmax, smart_sum)