def bfs():
    while q:
        r, c =q.pop(0)
        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]
            if 0 <= new_r < N and 0 <= new_c < N:
                if arr[new_r][new_c] > int(data[new_r][new_c]) + arr[r][c]:
                    arr[new_r][new_c] = int(data[new_r][new_c]) + arr[r][c]
                    q.append((new_r, new_c))


N = int(input())
data = [list(input()) for _ in range(N)]
arr = [[987654321]*N for _ in range(N)]
q = []
arr[0][0] = 0
q.append((0, 0))
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
bfs()
print(arr[-1][-1])