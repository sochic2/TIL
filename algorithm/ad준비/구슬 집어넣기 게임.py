def bfs():
    global solution
    while q:
        a = q.pop(0)
        cnt = a[0]
        red_r = a[1]
        red_c = a[2]
        blue_r = a[3]
        blue_c = a[4]
        if red_r == blue_c and red_c == blue_c: continue
        if cnt > 10: continue

        for i in range(4):
            nred_r = red_r + dr[i]
            nred_c = red_c + dc[i]
            nblue_r = blue_r + dr[i]
            nblue_c = blue_c + dc[i]
            if 0 <= nred_r < R and 0 <= nblue_r < R and 0 <= nred_c < C and 0 <= nblue_c < C:
                if data[nred_r][nred_c] == '#':
                    if data[nblue_r][nblue_c] == '#' and [cnt+1, red_r, red_c, blue_r, blue_c] not in stack:
                        q.append([cnt+1, red_r, red_c, blue_r, blue_c])
                        stack.append([cnt+1, red_r, red_c, blue_r, blue_c])
                    if data[nblue_r][nblue_c] == '.' and [cnt+1, red_r, red_c, nblue_r, nblue_c] not in stack:
                        q.append([cnt+1, red_r, red_c, nblue_r, nblue_c])
                        stack.append([cnt+1, red_r, red_c, nblue_r, nblue_c])

                if data[nred_r][nred_c] == '.':
                    if data[nblue_r][nblue_c] == '#' and [cnt+1, nred_r, nred_c, blue_r, blue_c] not in stack:
                        q.append([cnt+1, nred_r, nred_c, blue_r, blue_c])
                        stack.append([cnt+1, nred_r, nred_c, blue_r, blue_c])
                    if data[nblue_r][nblue_c] == '.' and [cnt+1, nred_r, nred_c, nblue_r, nblue_c] not in stack:
                        q.append([cnt+1, nred_r, nred_c, nblue_r, nblue_c])
                        stack.append([cnt+1, nred_r, nred_c, nblue_r, nblue_c])

                if data[nred_r][nred_c] == 'H':
                    if cnt +1  < solution:
                        solution = cnt +1









T = int(input())
for tc in range(T):
    R, C = map(int, input().split())
    data = [list(input()) for _ in range(R)]

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    ball = [0, 0, 0, 0, 0]
    for r in range(R):
        for c in range(C):
            if data[r][c] == 'R':
                ball[1] = r
                ball[2] = c
                data[r][c] = '.'
            if data[r][c] == 'B':
                ball[3] = r
                ball[4] = c
                data[r][c] = '.'
            if data[r][c] == 'H':
                goal_r = r
                goal_c = c
    solution = 987654321
    q = []
    stack =[]
    q.append(ball)
    stack.append(ball)
    bfs()
    if solution == 987654321:
        print(-1)
    else:
        print(solution)