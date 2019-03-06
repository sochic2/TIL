import sys
sys.stdin = open('호수의깊이.txt')
N = int(input())

lake = [list(map(int, input().split())) for _ in range(N)]

solution = 0
for i in range(N):
    for j in range(N):
        if lake[i][j] == 1:
            for k in range(1, N):
                if lake[i+k][j] == 0:
                    solution += k
                    break
                elif lake[i-k][j] == 0:
                    solution += k
                    break
                elif lake[i][j+k] == 0:
                    solution += k
                    break
                elif lake[i][j-k] == 0:
                    solution += k
                    break

print(solution)