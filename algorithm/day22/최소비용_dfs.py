def dfs(row, col, height, cost):
    global mmin
    if mmin > cost:
        return
    if row == N-1 and col == N-1:
        if mmin > cost:
            mmin = cost
        return

    for i in range(4):
        new_row = row + dy[i]
        new_col = row + dx[i]
        if new_row < 0 or new_col < 0 or new_row >= N or new_col >= N: continue
        if data[new_row][new_col] != -1:
            new_height = data[new_row][new_col]
            if new_height > height:
                data[new_row][new_col] = -1
                dfs(new_row, new_col, new_height, 1 + cost + (new_height - height))
                data[new_row][new_col] = new_height
            else:
                data[new_row][new_col] = -1
                dfs(new_row, new_col, new_height, cost + 1)
                data[new_row][new_col] = new_height




import sys
sys.stdin = open('최소비용.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    mmin = 987654321
    height = data[0][0]
    data[0][0] = -1
    dfs(0, 0, height, 0)
    print(mmin)