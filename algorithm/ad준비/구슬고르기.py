def hard(N, s):
    if N == s :
        print(*arr)
    else:
        for i in range(s, N):
            arr[i], arr[s] = arr[s], arr[i]
            hard(N, s+1)
            arr[i], arr[s] = arr[s], arr[i]

N = int(input())
arr = list(range(1, N+1))


hard(N, 0)
