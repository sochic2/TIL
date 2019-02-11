def dfs(v):
    global G, visited, n
    visited[v] = 1
    print(v, end=" ")

    for w in range(n):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)


import sys

sys.stdin = open('연습문제_input.txt')
# N = int(input())
# data = input()
#
# print(data)
# data_1 = list(data.split(' '))
# data_2 = list(map(int, data_1))
# print(data_2)

n, e= map(int, input().split())
n +=1
temp = list(map(int, input().split()))

G = [[0 for i in range(n)]for j in range(n)] # 2차원 초기화
visited = [0 for i in range(n)]

for i in range(0, len(temp), 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

for i in range(n):
    print(f'{i}{G[i]}')



dfs(1)







