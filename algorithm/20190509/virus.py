def bfs():
    global result
    visited = [[0] * N for _ in range(N)]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]


    while q:
        r, c, ccount = q.pop(0)
        visited[r][c] = ccount +1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == 0 and data[nr][nc] != 1:
                    q.append((nr, nc, ccount+1))
                    visited[nr][nc] = ccount+1


    solution = -987654321
    for i in range(N):
        for j in range(N):
            if visited[i][j] > solution:
                solution = visited[i][j]
    if solution < result:
        result = solution

    for i in visited:
        print(*i)
    print()

print('애기또리')



def hard(c, k):
    global M
    if c == M :
        print(q)
        bfs()
        return


# bfs 함수 ㄱㄱ
    else:
        for i in range(k, len(place) - M + c +1 ):
            q.append(place[i])
            hard(c+1, i+1)
            if len(q):
                q.pop(-1)



N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
place = []
for r in range(N):
    for c in range(N):
        if data[r][c] == 2:
            place.append((r, c, 0))

# print(place)
q = []
result = 987654321
hard(0, 0)
print(result)

