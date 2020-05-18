answer = 987654321
def solution(board):


    N = len(board)
    # board[N-1][N-1] = 3
    # print(N)
    visited = [[0]*N for _ in range(N)]
    # print(visited)

    visited[0][0] = 9
    # dx = [0, 1, 0, -1]
    # dy = [1, 0, -1, 0]

    # count_corner = 0
    # check_corner = [0, 0]

    def DFS(x, y, cost, count_corner, check_corner):
        global answer

        # visited[x][y] = 9

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        if answer < cost:
            return

        if x == N-1 and y == N-1:
            if answer >= (cost+100) + (count_corner*500):
                answer = (cost+100) + (count_corner*500)
            return answer
            # return (cost+100) + (count_corner*500)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if board[nx][ny] == 1:
                continue

            # if board[nx][ny] == 3:
            #     # if answer >= cost:
            #     #     answer = cost
            #     return (cost+100) + (count_corner*500)
            #     # return cost

            if board[nx][ny] == 0 and visited[nx][ny] == 0:
                if i == 0:
                    check_corner[0] = 1
                if i == 1:
                    check_corner[1] = 1
                if i == 2:
                    check_corner[0] = 1
                if i == 3:
                    check_corner[1] = 1

                if check_corner == [1, 1]:
                    count_corner += 1
                    check_corner = [0, 0]

                visited[nx][ny] = 9
                DFS(nx, ny, cost+100, count_corner, check_corner)
                # DFS(nx, ny, (cost+100) + (count_corner*500), count_corner, check_corner)
                visited[nx][ny] = 0

    DFS(0, 0, 0, 0, [0, 0])

    return answer

# board = [[0, 0], [0, 0]]
# answer = 987654321

# board = [[0,0,0],[0,0,0],[0,0,0]]
# result = 900

# board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
# result = 3800
#
# board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
# result = 2100
#
# board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
# result = 3200

print(solution(board))