import sys
sys.stdin = open('핀볼.txt')

def direction_change(direction, block):  #d는 방향
    global result
    result += 1
    # direction 상, 하, 좌, 우
    if direction == 0:  # 상
        if block == 2:
            return 3
        elif block == 3:
            return 2
        else:
            return 1

    if direction == 1:  # 하
        if block == 1:
            return 3
        elif block == 4:
            return 2
        else:
            return 0

    if direction == 2:  # 좌
        if block == 2:
            return 1
        elif block == 1:
            return 0
        else:
            return 3

    if direction == 3:  # 우
        if block == 3:
            return 1
        elif block == 4:
            return 0
        else:
            return  2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 벽에 5 씌우기
    arr.append([5] * N)
    arr.insert(0, [5] * N)
    for i in arr:
        i.append(5)
        i.insert(0, 5)

    warmhole = [[] for _ in range(11)]

    for y in range(N+2):
        for x in range(N+2):
            if arr[y][x] > 5:
                warmhole[arr[y][x]].append([y, x])

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    solution = 0

    for y in range(N+2):
        for x in range(N+2):
            if arr[y][x] == 0:

                for i in range(4):
                    direction = i
                    ny = y + dy[i]
                    nx = x + dx[i]
                    result = 0
                    flag = 0
                    while arr[ny][nx] != -1:
                        if ny == y and nx == x:
                            break
                        else:
                            # 빈칸일때
                            if arr[ny][nx] == 0:
                                ny = ny + dy[direction]
                                nx = nx + dx[direction]

                            #  블록일때
                            if 1 <= arr[ny][nx] and arr[ny][nx] <= 5:
                                direction = direction_change(direction, arr[ny][nx])
                                if direction == 0:
                                    ny = ny -1
                                    nx = nx
                                if direction == 1:
                                    ny = ny + 1
                                    nx = nx
                                if direction == 2:
                                    ny = ny
                                    nx = nx-1
                                if direction == 3:
                                    ny = ny
                                    nx = nx+1

                            # 웜홀일때
                            if 5 < arr[ny][nx] and arr[ny][nx] < 11:
                                nny = ny
                                nnx = nx
                                if warmhole[arr[ny][nx]][0] == [ny, nx]:
                                    ny = warmhole[arr[nny][nnx]][1][0] + dy[direction]
                                    nx = warmhole[arr[nny][nnx]][1][1] + dx[direction]
                                else:
                                    ny = warmhole[arr[nny][nnx]][0][0] + dy[direction]
                                    nx = warmhole[arr[nny][nnx]][0][1] + dx[direction]

                    if result > solution:
                        solution = result

    print('#{} {}'.format(tc, solution))