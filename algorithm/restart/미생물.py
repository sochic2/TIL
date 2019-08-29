import sys
sys.stdin = open('미생물.txt')

def ssum(fakedic):
    for key in fakedic.keys():
        cnts = fakedic[key][0]
        directions = fakedic[key][1]
        if len(cnts) > 1:
            newdirection = [directions[cnts.index(max(cnts))]]
            newcnts = [sum(cnts)]
            fakedic[key] = [newcnts, newdirection]
    return fakedic




def check(dic):
    global M
    dy = [0, -1, 1, 0, 0]
    dx = [0, 0, 0, -1, 1]
    for z in range(M):
        fakedic = {}
        flag = 0
        for key in dic.keys():
            y = key[0]
            x = key[1]
            cnt = dic[key][0][0]
            direction = dic[key][1][0]
            ny = y + dy[direction]
            nx = x + dx[direction]
            if ny == 0 or ny == N - 1 or nx == 0 or nx == N - 1:
                cnt = cnt // 2
                if direction == 1:
                    direction = 2
                elif direction == 2:
                    direction = 1
                elif direction == 3:
                    direction = 4
                elif direction == 4:
                    direction = 3

            if (ny, nx) in fakedic:
                flag = 1
                fakedic[(ny, nx)][0].append(cnt)
                fakedic[(ny, nx)][1].append(direction)

            else:
                fakedic[(ny, nx)] = [[cnt], [direction]]

        if flag == 1:
            dic = ssum(fakedic)
        else:
            dic = fakedic

    result = 0
    for i in dic.keys():
        result += dic[i][0][0]
    return result

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]
    # 세로, 가로, 미생물 수, 방향
    dic = {}
    for i in arr:
        y = i[0]
        x = i[1]
        cnt = i[2]
        direction = i[3]
        dic[(y, x)] = [[cnt], [direction]]
    solution = check(dic)


    print('#{} {}'.format(tc, solution))
