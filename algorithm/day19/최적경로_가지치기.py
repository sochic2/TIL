import sys
import time

sys.stdin = open('최적경로.txt')
start_time = time.time()
# def ssum():
#     global N, min
#     plus = 0
#     plus += abs(company[0] - data[arr[0]*2]) + abs(company[1] - data[arr[0]*2 +1])
#     t = 0
#     while t != N-1:
#         plus += abs(data[arr[t]*2] - data[arr[t+1]*2]) + abs(data[arr[t]*2 + 1] - data[arr[t+1]*2 +1] )
#         if plus > min:
#             return
#         t += 1
#
#     plus += abs(data[arr[-1]*2] - home[0]) + abs(data[arr[-1]*2 +1] - home[1])
#
#     if plus < min :
#         min = plus

def perm(n, k):
    global min, plus

    if k == n :
        if plus < min:
            min = plus
        return

    else:
        plus = 0
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            if i == 0:
                plus += abs(data[0] - data[arr[0] * 2]) + abs(data[1] - data[arr[0] * 2 + 1])
            elif i == n-1:
                plus += abs(data[-2] - data[arr[-1] * 2]) + abs(data[-1] - data[arr[-1] * 2 + 1])

            else:
                plus += abs(data[arr[i] *2] - data[arr[i+1]*2]) + abs(data[arr[i] *2 +1] - data[arr[i+1]*2+1])

            if plus > min:
                return

            perm(n, k+1)
            arr[i], arr[k] = arr[k], arr[i]




T = 10
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))


    data.append(data.pop(2))
    data.append(data.pop(2))
    arr = list(range(1, N+1))
    min = 987654321


    perm(N, 0)
    print('#{} {}'.format(tc, min))
print(time.time() - start_time, 'seconds')

