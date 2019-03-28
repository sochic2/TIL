# 중복순열    6*5*4
def hard(N, s):
    global M
    if N == s :
        if sum(arr) == M:
            print(*arr)
    else:
        for i in dice:
            arr[s] = i
            hard(N, s+1)

N, M = map(int, input().split())
dice = [1, 2, 3, 4, 5, 6]

arr = [0] * N

hard(N, 0)

