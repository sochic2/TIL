import copy
dy = [1, 0]
dx = [0, 1]
answer = 0



def down(c_board):
    flag = 0
    for yyy in range(len(c_board)-1, -1, -1):
        for xxx in range(len(c_board)):
            if c_board[yyy][xxx] == 0:
                for i in range(yyy, -1, -1):
                    if c_board[i][xxx] != 0:
                        c_board[yyy][xxx], c_board[i][xxx] = c_board[i][xxx], c_board[yyy][xxx]
                        flag = 1
                        break
    if flag == 1:
        start(c_board)



def start(c_board):
    global answer
    flag = 0
    vvisit = [[0]*len(c_board) for _ in range(len(c_board))]
    for yy in range(len(c_board)):
        for xx in range(len(c_board)):
            if c_board[yy][xx] == 0:continue
            candy = c_board[yy][xx]
            for i in range(2):
                visit = [(yy, xx)]
                q = [(yy, xx)]
                while q:
                    y, x = q.pop(0)
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or nx < 0 or ny >= len(c_board) or nx >= len(c_board):continue
                    if c_board[ny][nx] == candy:
                        q.append((ny, nx))
                        visit.append((ny, nx))
                if len(visit) >= 3:
                    flag = 1
                    for i in visit:
                        vvisit[i[0]][i[1]] = 1
    for y in range(len(vvisit)):
        for x in range(len(vvisit)):
            if vvisit[y][x] == 1:
                c_board[y][x] = 0

    if flag == 1:
        down(c_board)




def solution(board):
    global answer
    for y in range(1, len(board)):
        for x in range(len(board)):
            c_board = copy.deepcopy(board)
            c_board[y][x] = 0
            down(c_board)
            result = 0
            for r in range(len(board)):
                for c in range(len(board)):
                    if c_board[r][c] == 0:
                        result +=1
            if result > answer:
                answer = result




    return answer



board = [[1,1,3,3],[4,1,3,4],[1,2,1,1],[2,1,3,2]]

print(solution(board))