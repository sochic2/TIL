import sys
sys.stdin = open('전기카트.txt')
T = int(input())

def ssum():
    global N, mmin
    plus = 0

    plus += data[0][arr[0]]
    for i in range(N-2):
        plus += data[arr[i]][arr[i+1]]
    plus += data[arr[-1]][0]
    if plus < mmin:
        mmin = plus

def perm(n, k):
    global min

    if k == n:
        # print(arr)
        ssum()
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k + 1)
            arr[i], arr[k] = arr[k], arr[i]


for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(data)
    arr = list(range(1, N))
    mmin = 987654321
    perm(N-1, 0)
    print('#{} {}'.format(tc, mmin))

