def dfs(no):
    global mmin
    if no == N-1:
        ssum =0
        for i in range(N):
            if data[arr[i]][arr[i+1]] == 0:
                return
            else:
                ssum += data[arr[i]][arr[i+1]]
        if ssum < mmin:
            mmin = ssum

    else:
        for i in range(1, N):
            if chk[i-1] == 0:
                if data[arr[no]][i] == 0:continue

                chk[i-1] = 1
                arr[no+1] = i
                dfs(no+1)
                chk[i-1] = 0
                arr[no+1] = 0


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
chk = [0] * (N-1)
arr = [0] * (N+1)
mmin = 987654321
dfs(0)
print(mmin)