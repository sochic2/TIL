data = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

ih = [[0 for j in range(9)] for i in range(9)]

for i in range(0, len(data), 2):
    ih[data[i]][data[i+1]] = 1
    ih[data[i+1]][data[i]] = 1


def BFS(data, v):
    queue = []
    queue.append(v)
    print(v, end=' ')
    visit = [0] * (max(data)+1)

    visit[v] = 1
    while len(queue) !=0:
        t = queue.pop(0)
        for i in range(1, max(data)+1):
            if ih[t][i] == 1 and visit[i] ==0:
                queue.append(i)
                visit[i] = visit[t] +1
                print(i, end=' ')
    print(visit)

BFS(data, 1)