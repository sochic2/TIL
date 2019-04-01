def perm(n, k, ssum):
    global mmin
    if ssum > mmin:
        return
    else:
        if n == k:
            if ssum < mmin:
                mmin = ssum
        else:
            for i in range(n):
                if chk[i] == 0:
                    chk[i] = 1
                    perm(n, k+1, ssum + arr[k][i])
                    chk[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mmin = 987654321
    cookie = list(map(int, input().split()))
    robot = list(map(int, input().split()))
    chk = [0] * N
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = abs(cookie[i*2] - robot[j*2]) + abs(cookie[i*2+1] - robot[j*2 +1])

    perm(N, 0, 0)
    print(mmin)