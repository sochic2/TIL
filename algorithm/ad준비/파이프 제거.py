def up_chk(row, col):
    if row -1 >= 0:
        if data[row-1][col] in up:
            q.append((row - 1, col, data[row-1][col]))
            data[row-1][col] = '0'
    else:
        return

def down_chk(row, col):
    if row + 1 < N:
        if data[row+1][col] in down:
            q.append((row+1, col, data[row+1][col]))
            data[row+1][col] ='0'
    else: return

def right_chk(row, col):
    if col + 1 < N:
        if data[row][col+1] in right:
            q.append((row, col + 1, data[row][col+1]))
            data[row][col+1] = '0'
    else:
        return

def left_chk(row, col):
    if col-1 >= 0:
        if data[row][col-1] in left:
            q.append((row, col-1, data[row][col-1]))
            data[row][col-1] = '0'
    else:
        return




def bfs():
    while q:
        row, col, pipe = q.pop(0)

        if pipe == '1':
            left_chk(row, col)
            right_chk(row, col)

        if pipe == '2':
            up_chk(row, col)
            down_chk(row, col)

        if pipe == '3':
            right_chk(row, col)
            down_chk(row, col)

        if pipe == '4':
            left_chk(row, col)
            down_chk(row, col)

        if pipe == '5':
            up_chk(row, col)
            left_chk(row, col)

        if pipe == '6':
            up_chk(row, col)
            right_chk(row, col)

        if pipe == '7':
            up_chk(row, col)
            right_chk(row, col)
            down_chk(row, col)

        if pipe == '8':
            left_chk(row, col)
            right_chk(row, col)
            down_chk(row, col)

        if pipe == '9':
            left_chk(row, col)
            up_chk(row, col)
            down_chk(row, col)

        if pipe == 'A':
            left_chk(row, col)
            right_chk(row, col)
            up_chk(row, col)
        if pipe == 'B':
            left_chk(row, col)
            right_chk(row, col)
            up_chk(row, col)
            down_chk(row, col)


N = int(input())
X, Y = map(int, input().split())
data = [list(input()) for _ in range(N)]

left = ['1', '3', '6', '7', '8', 'A', 'B']
right = ['1', '4', '5', '8', '9', 'A', 'B']
up = ['2', '3', '4', '7', '8', '9', 'B']
down = ['2', '5', '6', '7', '9', 'A', 'B']



q = []
q.append((Y, X, data[Y][X]))
data[Y][X] = '0'
bfs()
ssum = N*N
for i in data:
    ssum -= i.count('0')

print(ssum)