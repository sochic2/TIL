def dfs(v):
    global G, visited, n
    s =[]

    s.append(v)
    while len(s) != 0:
        v = s.pop()
        if not visited[v]:
            visited[v] = 1
            print(v, end=" ")
            # for w in range(n-1, 0, -1):  #반대로 돌림 전꺼랑 같은 답 나오게
            for w in range(1, n):
                if G[v][w] == 1 and visited[w] ==0:
                    s.append(w)



import sys

sys.stdin = open('연습문제_input.txt')


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