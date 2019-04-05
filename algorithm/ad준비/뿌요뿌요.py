def down():
    fflag = 0

    for r in range(11, -1, -1):
        for c in range(6):
            if data[r][c] in ball:
                for i in range(11, r, -1):
                    if data[i][c] == '.':
                        fflag = 1
                        data[i][c], data[r][c] = data[r][c], data[i][c]

                        break

    if fflag == 1:

        bfs(data)
    else:
        return

def bfs(data):
    global solution
    flag = 0

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    for Y in range(12):
        for X in range(6):
            q = []
            visited = []
            if data[Y][X] in ball:
                q.append((Y,X))
                visited.append((Y,X))
                while q:
                    r, c = q.pop(0)
                    for i in range(4):
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if 0 <= nr < 12 and 0 <= nc < 6:
                            if data[r][c] == data[nr][nc] and (nr, nc) not in visited:
                                q.append((nr, nc))
                                visited.append((nr, nc))
                if len(visited) >= 4:
                    flag = 1
                    while visited:
                        r, c = visited.pop(0)
                        data[r][c] = '.'

    if flag == 1:
        solution += 1
        down()
    else:
        return






T = int(input())
for tc in range(1, T+1):
    data = [list(input()) for _ in range(12)]
    # print(data)
    solution = 0
    ball = ['R', 'G', 'B', 'P', 'Y']


    bfs(data)

    print(solution)