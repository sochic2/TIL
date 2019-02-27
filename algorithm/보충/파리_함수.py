def get_sum(i, j):
    global M
    sum = 0
    for x in range(M):
        for y in range(M):
            sum += data[i + x][j +y]

    return sum





import sys
sys.stdin = open('파리_input.txt')




T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = []
    for i in range(N):
        data += [list(map(int, input().split()))]



    max = 0
    min = 987654321

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = get_sum(i, j)
            if sum > max:
                max = sum
            if min > sum: min = sum
    print(f'#{tc} {max} {min}')



