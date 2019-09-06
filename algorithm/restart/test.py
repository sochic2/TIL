import sys
sys.stdin = open('미세먼지 안녕.txt')


def cleaner_on(aircleaner, data):

    # 위쪽 같은 행
    temp1 = 0
    temp1 = data[aircleaner[0][0]][C-1]
    data[aircleaner[0][0]][C-1] = 0

    for i in range(C-2, 0, -1):
        data[aircleaner[0][0]][i+1] = data[aircleaner[0][0]][i]
    data[aircleaner[0][0]][1] = 0

    # 열 맨 끝
    temp2 = data[0][C-1]
    data[0][C-1] = 0

    for i in range(0, aircleaner[0][0]):
        data[i][C-1] = data[i+1][C-1]
    data[aircleaner[0][0]-1][C-1] = temp1

    # 맨 위 행
    temp3 = data[0][0]
    data[0][0] = 0

    for i in range(1, C-1):
        data[0][i] = data[0][i+1]
    data[0][C-2] = temp2

    # 열 맨 앞
    temp4 = data[aircleaner[0][0]-1][0]
    data[aircleaner[0][0]-1][0] = 0

    for i in range(aircleaner[0][0]-1, -1, -1):
        data[i][0] = data[i-1][0]
    data[0][0] = temp4


    # 아래쪽 같은 행
    temp5 = 0
    temp5 = data[aircleaner[1][0]][C-1]
    data[aircleaner[1][0]][C-1] = 0

    for i in range(C-2, 0, -1):
        data[aircleaner[1][0]][i+1] = data[aircleaner[1][0]][i]
    data[aircleaner[1][0]][1] = 0

    # 열 맨 끝
    temp6 = data[R-1][C-1]
    data[R-1][C-1] = 0

    for i in range(R-1, aircleaner[1][0], -1):
        data[i][C-1] = data[i-1][C-1]
    data[aircleaner[1][0]+1][C-1] = temp5

    # 행 맨 끝
    temp7 = data[R-1][0]
    data[R-1][0] = 0

    for i in range(0, C-1):
        data[R-1][i] = data[R-1][i+1]
    data[R-1][C-2] = temp6

    # 열 맨 앞
    temp8 = data[aircleaner[1][0]+1][0]
    data[aircleaner[1][0]+1][0] = 0

    for i in range(aircleaner[1][0]+1, R-1):
        data[i][0] = data[i+1][0]
    data[R-2][0] = temp7


def spread(q):
    global new, origin

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while len(q) != 0:
        ax, ay = q.pop(0)

        count = 0
        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if data[nx][ny] == -1:
                continue
            else:
                if (nx, ny) not in new:
                    new[(nx, ny)] = data[ax][ay]//5
                    count += 1
                elif (nx, ny) in new:
                    new[(nx, ny)] += data[ax][ay]//5
                    count += 1

        # origin[(ax, ay)] = data[ax][ay] - ((data[ax][ay] // 5) * count)
        if (ax, ay) not in new:
            new[(ax, ay)] = data[ax][ay] - ((data[ax][ay] // 5) * count)
        elif (ax, ay) in new:
            new[(ax, ay)] += data[ax][ay] - ((data[ax][ay] // 5) * count)

R, C, T = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(R)]


aircleaner = []
while T > 0:
    # 공기청정기 위치 & 미세먼지 위치
    dust = []
    new = {}
    # origin = {}
    for i in range(R):
        for j in range(C):
            if data[i][j] == -1:
                aircleaner.append((i, j))
            elif data[i][j] != -1 and data[i][j] != 0:
                dust.append((i, j))

    spread(dust)
    # 방 초기화
    for i in range(R):
        for j in range(C):
            data[i][j] = 0

    # 공기청정기 설치
    data[aircleaner[0][0]][aircleaner[0][1]] = -1
    data[aircleaner[1][0]][aircleaner[1][1]] = -1

    # 먼지 계산
    for i in new.keys():
        data[i[0]][i[1]] += new.get(i)

    # for i in origin.keys():
    #     data[i[0]][i[1]] += origin.get(i)

    # 공기청정기 작동
    cleaner_on(aircleaner, data)
    T -= 1

# 먼지 합
total = 0
for i in range(R):
    for j in range(C):
        if data[i][j] != 0:
            total += data[i][j]
print(total+2)