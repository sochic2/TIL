import sys
sys.stdin = open('회문.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    data = [input() for _ in range(8)]

    x_result = 0
    y_result = 0
    for i in range(8):
        for j in range(8-N+1 ):
            count = 0
            for o in range(N//2):
                if data[i][j+o] == data[i][j-o +N-1]:
                    count += 1
            if count == N//2:
                x_result +=1



    for k in range(8):
        for l in range(8 -N+1):
            count = 0
            for o in range(N//2):
                if data[l+o][k] == data[l-o+ N-1][k]:
                    count += 1
            if count == N//2:
                y_result +=1

    print('#{} {}'.format(tc, y_result))
    print(x_result, y_result)