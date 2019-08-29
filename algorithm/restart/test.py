import copy

def BFS(x, y, distance, chance, temp):
    global result
    q = []
    q.append((x, y, distance, chance, temp))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while len(q) != 0:
        ax, ay, distance, chance, temp = q.pop(0)

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            # 벽처리
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 길 0이 갈수있는곳, 1이 벽
            if temp[nx][ny] != 0 and chance == 0:
                continue
            # chance
            if temp[nx][ny] != 0 and chance == 1:
                # temp[nx][ny] = 0
                visited[nx][ny] = distance+1
                q.append((nx, ny, distance+1, 0, temp))
                # temp[nx][ny] = 1

            # 탈출
            if nx == N-1 and ny == M-1:
                visited[nx][ny] = distance+1
                # for i in visited:
                #     print(i)
                if result > distance+1:
                    result = distance+1
                    return result
            # 이동
            if temp[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = distance+1
                q.append((nx, ny, distance+1, chance, temp))
    return -1

N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
temp = copy.deepcopy(data)
# print(data)
# print(visited)

result = 987654321
visited[0][0] = 1
print(BFS(0, 0, 1, 1, temp))