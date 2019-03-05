import sys
sys.stdin = open('자리배치.txt')

C, R = map(int, input().split())
K = int(input())

paper = [[0 for _ in range(C)] for _ in range(R)]


count = 1

x = 0
y = R
a, b = C, R

while count < C*R +1:
    for i in range(b):
        paper[y-1][x] = count
        count += 1
        y -= 1

    for i in range(a-1):
        paper[y][x+1] = count
        count += 1
        x += 1

    for i in range(b-1):
        paper[y+1][x] = count
        count +=1
        y += 1

    for i in range(a-2):
        paper[y][x-1] = count
        count += 1
        x-= 1

    a -= 2
    b -= 2

solution = 0

for i in range(C):
    for j in range(R):
        if paper[j][i] == K:
            z = R-j
            x = 1+i
            solution = 1
if solution == 1:
    print('{} {}'.format(x, z))
else:
    print(0)