import sys
sys.stdin = open('낚시왕.txt')

def move(sharks, sharks_detail):
    newsharks = []
    newsharks_detail = []
    for i in range(len(sharks)):
        y, x, s, d, z = sharks[i][0], sharks[i][1], sharks_detail[i][0], sharks_detail[i][1], sharks_detail[i][2]
        ns = s
        while ns != 0:
            if d == 1:
                if y + dy[d] == 0:
                    d = 2
            if d == 2:
                if y + dy[d] == Y+1:
                    d = 1
            if d == 3:
                if x + dx[d] >= X+1:
                    d = 4
            if d == 4:
                if x + dx[d] <= 0:
                    d = 3
            y += dy[d]
            x += dx[d]
            ns -= 1

        if (y, x) in newsharks:
            if newsharks_detail[newsharks.index((y, x))][2] < z:
                newsharks_detail[newsharks.index((y, x))] = (s, d, z)
        else:
            newsharks.append((y, x))
            newsharks_detail.append((s, d, z))
    return newsharks, newsharks_detail

def find(start, sharks, sharks_detail):
    global result

    for i in range(Y+1):
        for j in range(len(sharks) - 1, -1, -1):
            if sharks[j] == (i, start):
                result += sharks_detail[j][2]
                sharks.pop(j)
                sharks_detail.pop(j)
                return



Y, X, M= map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
# x, y, 속력, 이동방향, 크기
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]
start = 1
result = 0
sharks = []
sharks_detail = []
for i in range(M):
    y, x, s, d, z= arr[i][0], arr[i][1], arr[i][2], arr[i][3], arr[i][4]
    sharks.append((y, x))
    sharks_detail.append((s, d, z))

while start != X+1:
    find(start, sharks, sharks_detail)

    sharks, sharks_detail = move(sharks, sharks_detail)


    start += 1




print(result)