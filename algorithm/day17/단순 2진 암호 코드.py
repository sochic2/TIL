import sys
sys.stdin = open('단순 2진 암호코드.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    psw = [[0, 0, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 0, 1],
           [0, 0, 1, 0, 0, 1, 1],
           [0, 1, 1, 1, 1, 0, 1],
           [0, 1, 0, 0, 0, 1, 1],
           [0, 1, 1, 0, 0, 0, 1],
           [0, 1, 0, 1, 1, 1, 1],
           [0, 1, 1, 1, 0, 1, 1],
           [0, 1, 1, 0, 1, 1, 1],
           [0, 0, 0, 1, 0, 1, 1]
    ]

    flag = 0
    data = [list(map(int, input())) for _ in range(N)]
    # print(data)
    for i in range(len(data)):
        if flag == 1:
            break
        if sum(data[i]) != 0:
            for j in range(M-56):

                if flag == 1:
                    break
                result = []
                if data[i][j:j+7] in psw:

                    for k in range(0, 8):
                        if data[i][j + 7 * k:j + (7 * (k + 1))] not in psw:
                            break
                        else:

                            for l in range(len(psw)):
                                if psw[l] == data[i][j+7*k:j+(7*(k+1))]:
                                    result += [l]
                                if len(result) == 7:
                                    flag = 1



    ssol = 0
    ssol_2 = 0
    for i in range(7):
        if not i % 2:
            ssol += result[i]
        else:
            ssol_2 += result[i]


    if not (ssol * 3 + ssol_2 + result[7]) % 10:
        print('#{} {}'.format(tc, sum(result)))
    else:
        print('#{} {}'.format(tc, 0))




