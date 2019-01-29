import sys
sys.stdin = open("회문_input.txt")
T = int(input())

for tc in range(T):
    dummy = input().split()
    N, M = int(dummy[0]), int(dummy[1])
    # print(T, N, M)
    data = []
    for i in range(N):
        data.extend([input()])
    # print(data)
    result = []
    if N != M:
        for j in range(N-M+1):
            for o in range(N):
                if data[o][j] == data[o][j+M-1]:
                    for p in range(M//2):
                        if data[o][j+p] != data[o][j+M-1-p]:
                            break
                    else:
                        print(f'#{tc + 1}', end=' ')
                        print(data[o][j:j+M])
    else:
        for o in range(N):
            if data[o][0] == data[o][M - 1]:
                for p in range(M // 2):
                    if data[o][p] != data[o][M - 1 - p]:
                        break
                else:
                    print(f'#{tc + 1}', end=' ')
                    print(data[o])

    if N != M:
        for j in range(N-M+1):
            for o in range(N):
                if data[j][o] == data[j+M-1][o]:
                    for p in range(M//2):
                        if data[j+p][o] != data[j+M-1-p][o]:
                            break
                    else:
                        for k in range(M):
                            result += list(data[k+j][o])
                        print(f'#{tc+1}',end=' ')
                        print(''.join(result))
    else:
        for o in range(N):
            if data[0][o] == data[M - 1][o]:

                for p in range(M // 2):
                    if data[p][o] != data[M - 1 - p][o]:
                        break
                else:
                    for k in range(M):
                        result += list(data[k][o])
                    print(f'#{tc + 1}', end=' ')
                    print(''.join(result))





