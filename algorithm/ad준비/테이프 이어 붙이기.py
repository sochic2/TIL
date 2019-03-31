def dfs(n, k, c,ssum):
    global mmin, ssum_2
    if n == k:
        if abs(sum(data) - (ssum * 2)) < mmin:
            mmin = abs(sum(data) - (ssum * 2))
            ssum_2 = sum(data) - ssum
    else:
        if c+1 > N:
            return
        else:
            chk[k] = data[c]
            dfs(n, k+1, c+1, ssum + data[c])
            chk[k] = 0
            dfs(n, k, c+1, ssum)


N = int(input())
data = list(map(int, input().split()))
ssum_2 = 0
mmin = 987654321
chk = [0] * (N//2)
dfs(N//2, 0, 0, 0)
print(mmin)