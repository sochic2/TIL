# -*- coding: utf-8 -*-

import sys
sys.stdin = open('테트로미노.txt')



## 최대 4개짜리 dfs로 전부 탐색하면됨
def dfs(x, y, visited, count, sumVal):
    global maxVal

    if count == 4:
        if maxVal < sumVal:
            maxVal = sumVal
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < m:
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                dfs(nx, ny, visited, count + 1, sumVal + arr[nx][ny])
                visited[nx][ny] = False


## ㅗ 모양은 dfs로 탐색이 안돼서 따로 처리해줌
## 가운데일 때를 기준으로 네방향 탐색
def fuck(x, y):
    global maxVal
    sumVal = arr[x][y]

    ## x, y가 모서리면 ㅗ 모양은 아예 불가능
    if x == 0:
        if y == 0 or y == m - 1:
            return
    elif x == n - 1:
        if y == 0 or y == m - 1:
            return

    ## x나 y가 가장자리에 있으면 ㅗ 모양은 하나밖에 안나옴
    if x == 0:
        sumVal += arr[x + 1][y] + arr[x][y - 1] + arr[x][y + 1]
    elif x == n - 1:
        sumVal += arr[x - 1][y] + arr[x][y - 1] + arr[x][y + 1]
    elif y == 0:
        sumVal += arr[x][y + 1] + arr[x - 1][y] + arr[x + 1][y]
    elif y == m - 1:
        sumVal += arr[x][y - 1] + arr[x - 1][y] + arr[x + 1][y]
    else:
        sumlist = []
        sumlist.append(sumVal + arr[x + 1][y] + arr[x][y - 1] + arr[x][y + 1])
        sumlist.append(sumVal + arr[x - 1][y] + arr[x][y - 1] + arr[x][y + 1])
        sumlist.append(sumVal + arr[x][y + 1] + arr[x - 1][y] + arr[x + 1][y])
        sumlist.append(sumVal + arr[x][y - 1] + arr[x - 1][y] + arr[x + 1][y])
        sumVal = max(sumlist)

    if maxVal < sumVal:
        maxVal = sumVal


def solve():
    visited = [[False] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            fuck(i, j)
            visited[i][j] = True
            dfs(i, j, visited, 1, arr[i][j])
            visited[i][j] = False



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
maxVal = 0

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

solve()
print(maxVal)