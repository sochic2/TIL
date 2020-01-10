n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]


def solution(n, computers):
    def dfs(y, start):
        for xx in range(n):
            if computers[y][xx] == 1 and visit[xx] == -1:
                visit[xx] = start
                dfs(xx, start)
    visit = [-1] * n
    for y in range(n):
        for x in range(n):
            if computers[y][x] == 1 and visit[x] == -1:
                dfs(x, y)
    visit_2 = set(visit)
    answer = len(visit_2)

    return answer





solution(n, computers)