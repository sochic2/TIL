def chk(no, i):
    global N
    for k in range(8):
        a = no + dy[k]
        b = i + dx[k]
        while True:
            if a < 0 or a >= N or b < 0 or b >= N:
                break
            else:
                if arr[a][b] == 1:
                    return False
                a += dy[k]
                b += dx[k]
    return True


def dfs(no):
    global cnt, N
    if no == N:
        cnt += 1
        return
    else:
        for i in range(N):
            if chk(no, i) and arr[no][i] == 0:
                arr[no][i] = 1
                dfs(no +1)
                arr[no][i] = 0


dx = [-1, 1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]

N = int(input())

cnt = 0

arr = [[0]*N for _ in range(N)]
dfs(0)
print(cnt)


