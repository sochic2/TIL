def dfs(r):
    global cnt
    if r == N:
        cnt += 1
    else:
        for c in range(N):
            if chk1[c] == 0 and chk2[r+c] == 0 and chk3[(N-1) - (r -c)] == 0:
                chk1[c] = 1
                chk2[r+c] = 1
                chk3[(N - 1) - (r - c)] = 1
                dfs(r+1)
                chk1[c] = 0
                chk2[r + c] = 0
                chk3[(N - 1) - (r - c)] = 0


N = int(input())
cnt = 0
chk1 = [0] * N
chk2 = [0] * N * 2
chk3 = [0] * N * 3
dfs(0)
print(cnt)