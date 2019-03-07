import sys
sys.stdin = open('연속부분최대곱.txt')
N = int(input())
data = []
for _ in range(N):
    data += [float(input())]




mmax = 0
mul = 1
for i in range(len(data)):
    if mul * data[i] < data[i]:
        mul = 1 * data[i]
        if mmax < mul:
            mmax = mul
    else:
        mul = mul * data[i]
        if mmax < mul:
            mmax = mul

print(format(mmax, '.3f'))
