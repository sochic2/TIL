def hard(k, n, ssum):
    global mmin, B
    if k == n:
        result.append(ssum)
    else:

        hard(k+1, n, ssum)

        arr[k] = 1
        hard(k+1, n, ssum + weight[k])
        hard(k+1, n, ssum - weight[k])
        arr[k] = 0


N = int(input())
weight = list(map(int, input().split()))
arr = [0] * N
result = []
gs = int(input())
gi = list(map(int, input().split()))

hard(0, N, 0)
for i in gi:
    if i in result:
        print('Y', end=' ')
    else:
        print('N', end=' ')