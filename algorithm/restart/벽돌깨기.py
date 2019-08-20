import sys, copy
sys.stdin = open('벽돌깨기.txt')


def perm(a):
    global N, result

    if a >= N:
        # print(parr)
        arr = copy.deepcopy(mapp)
        brick(arr)
        return
    else:
        for i in range(W):
            parr[a] = i
            perm(a + 1)
            parr[a] = 0


def down(arr):
    global H

    for x in range(W):
        flag = 0
        for y in range(H - 1, -1, -1):
            if arr[y][x] == 0 and flag == 0:
                for k in range(y, -1, -1):
                    if arr[k][x] != 0:
                        arr[y][x], arr[k][x] = arr[k][x], arr[y][x]
                        break
                    if k == 0 and arr[k][x] ==0:
                        flag = 1


def check(arr):
    global W, H
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while que:
        y, x, cnt = que.pop(0)
        if cnt != 1:
            for i in range(4):
                for j in range(1, cnt):
                    nx = x + dx[i] * j
                    ny = y + dy[i] * j

                    if nx < 0 or nx >= W or ny < 0 or ny >= H:
                        break
                    else:
                        if arr[ny][nx]:
                            que.append((ny, nx, arr[ny][nx]))
                            arr[ny][nx] = 0

    down(arr)
    return


def brick(arr):
    global H, result
    for i in range(len(parr)):
        for j in range(H):
            if arr[j][parr[i]] != 0:
                que.append((j, parr[i], arr[j][parr[i]]))
                arr[j][parr[i]] = 0
                check(arr)
                break
    ssum = 0
    for x in range(W):
        for y in range(H):
            if arr[y][x]:
                ssum += 1
    if ssum <= result:
        result = ssum


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    mapp = [list(map(int, input().split())) for _ in range(H)]
    parr = [0] * N
    # parr = [2, 2, 6]
    result = 987654321
    que = []

    perm(0)
    print('#{} {}'.format(tc, result))