import sys
sys.stdin = open('원안의마을.txt')
N = int(input())
town = [list(map(int, input())) for _ in range(N)]


result = 0

for i in range(N):
    for j in range(N):
        if town[i][j] == 2:
            telecom = [i,j]

for i in range(N):
    for j in range(N):
        if town[i][j] == 1:
            r  = ((telecom[0] - i) **2 + (telecom[1]-j) ** 2)**0.5
            if int(r) == r:
                if int(r) > result:
                    result = int(r)
            else:
                if int(r+1) > result:
                    result = int(r+1)

print(result)