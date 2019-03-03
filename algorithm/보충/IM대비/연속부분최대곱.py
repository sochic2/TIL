import sys
sys.stdin = open('연속부분최대곱.txt')
N = int(input())
data = []
for _ in range(N):
    data += [float(input())]


mmax = 0


for i in range(N):
    if data[i] > 1:
        result_mul = 1
        result_data = data[i::]
        for j in result_data:
            if j == 0:
                break
            result_mul *= j
            if result_mul > mmax:
                mmax = result_mul

if mmax == 0:
    print(format(max(data), '.3f'))
else:
    print(format(mmax, '.3f'))


