def hard(k, n, ssum):
    global mmin, B
    if k == n:
        if ssum < mmin and ssum>=B:
            mmin = ssum

    else:
        arr[k] = 0
        hard(k+1, n, ssum)
        if ssum + data[k] > mmin:
            return
        else:
            arr[k] = 1
            hard(k+1, n, ssum + data[k])

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    data = []
    for i in range(N):
        data.append(int(input()))

    arr = [0]*N

    mmin = 987654321

    hard(0, N, 0)

    print(mmin - B)