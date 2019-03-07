import sys
sys.stdin = open('비밀금고.txt')
N = int(input())
data = list(map(int, input().split()))

width = N * 2 -1

paper = [[0]*width for _ in range(width)]


for i in range(N):
    j = N-i-1
    for k in range(i+1):
        paper[i][j] = 1
        j += 2

for i in range(len(paper)-1, N-1, -1):
    j = i-N+1
    for k in range(2*N-i-1):
        paper[i][j] = 1
        j += 2

for i in range(len(paper)):
    for j in range(len(paper)):
        if paper[i][j] == 1:
            paper[i][j] = data.pop(0)

mmax = -987654321

for i in range(len(paper)):
    ssum = 0
    for j in range(len(paper)):
        ssum += paper[j][i]

    if ssum > mmax:
        mmax = ssum

print(mmax)

