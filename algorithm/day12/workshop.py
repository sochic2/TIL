import sys
sys.stdin = open('contact_input.txt')
def route(data, v):
    visited = [0] * (max(data) + 1)
    queue = []
    queue.append(v)
    visited[v] = 1

    while len(queue) != 0:
        t = queue.pop(0)
        for i in range(0, len(data), 2):
            if data[i] == t and visited[data[i+1]] == 0:
                queue.append(data[i+1])
                visited[data[i+1]] = visited[t]+1
    result = 0
    position = 0
    for i in range(len(visited)):
        if visited[i] >= result:
            result = visited[i]
            position = i
    # print(visited)
    # print(len(visited))
    print(f'#{tc} {position}')



T = 10
for tc in range(1, T+1):
    N, S = map(int, input().split())
    data = list(map(int, input().split()))

    route(data, S)


