import sys
sys.stdin = open('p2.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]
    atomdic = {}
    for i in range(len(atom)):
        atomdic[(atom[i][0]*2, atom[i][1]*2)] = [[atom[i][2]], [atom[i][3]]]
    # 상, 하, 좌, 우 0, 1, 2, 3
    # x, y, 이동방향, 보유에너지 K
    result = 0
    cnt = 0

    while cnt < 4000 and 1 < len(atom) :
        dy = [1, -1, 0, 0]
        dx = [0, 0, -1, 1]
        new = {}
        for i in atomdic.keys():
            if atomdic[i] == 0:
                continue
            x = i[0]
            y = i[1]
            direction = atomdic[i][0][0]
            K = atomdic[i][1][0]
            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx < -2005 or ny < -2005 or nx > 2005 or ny > 2005:continue
            if (nx, ny) in new:
                new[(nx, ny)][0].append(direction)
                new[(nx, ny)][1].append(K)
            else:
                new[(nx, ny)] = [[direction], [K]]

        for i in new.keys():
            if len(new[i][1]) > 1:
                result += sum(new[i][1])
                new[i] = 0
        atomdic = new

        cnt += 1


    print('#{} {}'.format(tc, result))