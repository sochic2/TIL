import sys
sys.stdin = open('파리_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = []
    for i in range(N):
        data += [list((map(int, input().split())))]


    result = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            max_fly = 0
            for k in range(M):
                for p in range(M):
                    max_fly += data[i+k][j+p]
                    # print(data[i+k][j+p])

            if max_fly > result:
                result = max_fly

    print(f'#{tc} {result}')



