import sys
sys.stdin = open('미로탈출 로봇.txt')

dr = [0, 1, 0, -1, 0]
dc = [0, 0, -1, 0, 1]

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

Darr = list(map(int, input().split()))

y_wall = [1] * (N+2)

for i in arr:
    i.append(1)
    i.insert(0, 1)
arr.append(y_wall)
arr.insert(0, y_wall)

Dno = 0
dr = [0, 1, 0, -1, 0]
dc = [0, 0, -1, 0, 1]
r, c = 1, 1
cnt = 0



while True:
    r = r+ dr[Darr[Dno]]
    c = c + dc[Darr[Dno]]
    if arr[r][c] == 0 :
        arr[r][c] = 9
        cnt += 1
    elif arr[r][c] == 1:
        r = r - dr[Darr[Dno]]
        c = c - dc[Darr[Dno]]
        Dno = (Dno +1) % 4
    else: break

print(cnt)
