import sys
sys.stdin = open('도넛츠 합계.txt')
N, K = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]


maxx = 0
for i in range(N-K+1):
    for j in range(N-K+1):
        ssum = 0
        for l in range(K):
            ssum += data[i][j+l]
            ssum += data[i+K-1][j+l]
            if ssum > maxx:
                maxx = ssum
        for m in range(1, K-1):
            ssum += data[i+m][j]
            ssum += data[i+m][j+K-1]
            if ssum > maxx:
                maxx = ssum

print(maxx)
