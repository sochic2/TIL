import copy, sys
sys.stdin = open('무선충전.txt')

T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    Amove = list(map(int, input().split()))
    Amove.insert(0, 0)
    Bmove = list(map(int, input().split()))
    Bmove.insert(0, 0)
    BC = [tuple(map(int, input().split())) for _ in range(A)]
    # BC의 X, Y 좌표, 충전범위, 처리량. 순서
    dy = [0, -1, 0, 1, 0]   # 이동안하고, 상, 우, 하, 좌
    dx = [0, 0, 1, 0, -1]

    BC.sort(key = lambda x: x[3])
    BC.reverse()

    Apoint = (1, 1)
    Bpoint = (10, 10)
    charge = 0
    charge1 = []
    charge2 = []
    B = []

    for i in range(M+1):

        Ay = Apoint[0] + dy[Amove[i]]
        Ax = Apoint[1] + dx[Amove[i]]
        By = Bpoint[0] + dy[Bmove[i]]
        Bx = Bpoint[1] + dx[Bmove[i]]
        Apoint = (Ay, Ax)
        Bpoint = (By, Bx)
        visitA = [0] * A
        visitB = [0] * A

        for j in range(len(BC)):
            BCy, BCx, C, P = BC[j][1], BC[j][0], BC[j][2], BC[j][3]
            if abs(BCy-Ay) + abs(BCx-Ax) <= C:
                visitA[j] = 1

            if abs(BCy-By) + abs(BCx-Bx) <= C:
                visitB[j] = 1

        result = 0
        for i in range(A):
            for j in range(A):
                resultA = 0
                resultB = 0
                if i == j:
                    if visitA[i] == 1 and visitB[j] == 1:
                        if result <= BC[i][3]:
                            result = BC[i][3]
                    else:
                        if visitA[i] == 1:
                            resultA = BC[i][3]
                        if visitB[j] == 1:
                            resultB = BC[j][3]
                        if result <= resultA + resultB:
                            result = resultA + resultB
                else:
                    if visitA[i] == 1:
                        resultA = BC[i][3]
                    if visitB[j] == 1:
                        resultB = BC[j][3]
                    if result <= resultA + resultB:
                        result = resultA + resultB
        charge += result

    print('#{} {}'.format(tc, charge))


