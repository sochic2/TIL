import sys
sys.stdin = open('달팽이사각형.txt')
n = int(input())

paper = [[0]*n for _ in range(n)]


count = 1
x = -1
y = 0

while count != n**2 +1:

    for i in range(n):
        paper[y][x+1] = count
        x += 1
        count += 1

    for j in range(n-1):
        paper[y+1][x] = count
        y += 1
        count += 1
    for k in range(n-1):
        paper[y][x-1] = count
        x -= 1
        count += 1
    for l in range(n-2):
        paper[y-1][x] = count
        y -=1
        count += 1
    n -= 2

for i in range(len(paper)):
    print(*paper[i])