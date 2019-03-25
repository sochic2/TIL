import sys
import time

sys.stdin = open('최적경로.txt')
start_time = time.time()
def ssum():
    global N, min
    plus = 0
    plus += abs(company[0] - data[arr[0]*2]) + abs(company[1] - data[arr[0]*2 +1])
    t = 0
    while t != N-1:
        plus += abs(data[arr[t]*2] - data[arr[t+1]*2]) + abs(data[arr[t]*2 + 1] - data[arr[t+1]*2 +1] )
        if plus > min:
            return
        t += 1

    plus += abs(data[arr[-1]*2] - home[0]) + abs(data[arr[-1]*2 +1] - home[1])

    if plus < min :
        min = plus

def perm(n, k):
    global min
    if k == n :
        # print(*arr)
        ssum()
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k+1)
            arr[i], arr[k] = arr[k], arr[i]




T = 10
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    company = []
    company.append(data.pop(0))
    company.append(data.pop(0))
    home = []
    home.append(data.pop(0))
    home.append(data.pop(0))
    arr = list(range(N))
    # print(data)
    # print(company)
    # print(home)
    min = 987654321

    # print(arr)
    perm(N, 0)
    print('#{} {}'.format(tc, min))
print(time.time() - start_time, 'seconds')

