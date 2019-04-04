def dfs(no):
    global flag
    if no == N:
        if flag == 0:
        # print(arr)
            for i in range(N):
                for j in range(len(data[i])):
                    if data[i][j]:
                        if arr[i] == arr[j]:
                            return
            print(*arr)
            flag = 1
            return

    else:
        for z in range(M):
            for i in range(no):
                for j in range(len(data[i])):
                    if data[i][j]:
                        if arr[i] == arr[j]:
                            return
            arr[no] = color[z]
            dfs(no+1)
            arr[no] = 0


N, M = map(int,input().split())
data = [list(map(int, input().split())) for _ in range(N)]
color = list(range(1, M+1))
arr = [0] * N
flag = 0
dfs(0)
if flag == 0:
    print(-1)