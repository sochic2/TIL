def binary(start, mmax):
    global solution
    s = start
    e = mmax
    bin = (s + e)//2
    ssum = 0
    for i in range(N):
        if tree[i] > bin:
            ssum += tree[i] - bin
    if ssum == M:
        solution = bin
        return
    elif ssum < M:
        binary(s, bin-1)
    elif ssum > M:
        binary(bin+1, e)




N, M = map(int, input().split())
tree = list(map(int, input().split()))
maxxx = max(tree)

solution = 0
binary(0, maxxx)
print(solution)