import sys
sys.stdin = open('노드의거리_input.txt')

def BFS(data, v):
    global G
    queue = []
    queue.append(v)

    visit = [0] * (V+1)

    visit[v] = 1
    while len(queue) !=0:
        t = queue.pop(0)
        for i in range(1, max(data)+1):
            if ih[t][i] == 1 and visit[i] ==0:
                queue.append(i)
                visit[i] = visit[t] +1
    result = 0
    if visit[G]:
        result = visit[G]-1

    print(f'#{tc} {result}')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = []
    for _ in range(E):
        data += list(map(int, input().split()))
    S, G = map(int,input().split())

    ih = [[0 for j in range(V+1)] for i in range(V+1)]

    for i in range(0, len(data), 2):
        ih[data[i]][data[i + 1]] = 1
        ih[data[i + 1]][data[i]] = 1

    BFS(data, S)
    