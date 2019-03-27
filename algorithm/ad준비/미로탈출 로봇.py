def bfs(s_y, s_x):
    global e_y, e_x
    flag = 0
    q = []
    q.append([s_y, s_x, 0])
    data[s_y][s_x] = 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        a = q.pop(0)
        if a[0] == e_y and a[1] == e_x:
            flag = 1
            return a[2]
        for i in range(4):
            if data[a[0] + dy[i]][a[1]+ dx[i]]==0:
                q.append([ a[0] + dy[i], a[1]+ dx[i], a[2]+1 ])
                data[ a[0] + dy[i]][a[1] + dx[i] ] = 1
    if flag == 0:
        return

X, Y = map(int, input().split())
s_x, s_y, e_x, e_y = map(int, input().split())
data = [[1] + list(map(int, input())) + [1] for _ in range(Y)]
y_wall = [1] * (X+2)
data.append(y_wall)
data.insert(0, y_wall)
# for i in data:
#     print(*i)
print(bfs(s_y, s_x))
