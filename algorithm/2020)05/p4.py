answer = 987654321

def solution(board):



    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    visit = [[999999]*len(board) for _ in range(len(board))]

    visit[0][0] = 0

    def dfs(y, x, charge, direction, n):
        global answer
        if y == len(board) - 1 and x == len(board) - 1:
            if charge < answer:
                answer = charge


        else:
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board):continue
                if board[ny][nx] == 1 or visit[ny][nx] < charge: continue

                if n == 0:
                    visit[ny][nx] = charge
                    dfs(ny, nx, charge+100, i, n+1)

                else:
                    if direction == i:
                        visit[ny][nx] = charge
                        dfs(ny, nx, charge+100, i, n+1)

                    else:
                        visit[ny][nx] = charge
                        dfs(ny, nx, charge+600, i, n+1)

    dfs(0, 0, 0, 0, 0)




    return answer




# 1
# board = [[0,0,0],[0,0,0],[0,0,0]]
# 2
board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]

print(solution(board))