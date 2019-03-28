cy = [[-1, -2, -3], [0, -1, -2], [0, 1, 2], [1, 2, 3], [1, 2, 3], [0, 1, 2], [0, -1, -2], [-1, -2, -3]]
cx = [[0, 1, 2], [1, 2, 3], [1, 2, 3], [0, 1, 2], [0, -1, -2], [-1, -2, -3], [-1, -2, -3], [0, -1, -2]]

def chk(r, c, i):
    zy = cy[i]
    zx = cx[i]
    for z in range(2):
        # if r + zy[z] < 0 or c + zx[z] < 0 or r + zy[z] >= 10 or c + zx[z] >= 10: return False

        if [r + zy[z], c + zx[z]] == [R2,C2]:
            return False
    return True



def BFS(y, x, num):
    q.append((y, x, num))
    arr[y][x] = 1
    while q:
        r, c, cnt = q.pop(0)
        if r == R2 and c == C2:
            print(cnt)
            return
        else:
            for i in range(8):
                if r + dy[i] < 0 or c + dx[i] < 0 or r + dy[i] >= 10 or c + dx[i] >= 9: continue
                if arr[r + dy[i]][c + dx[i]] == 0:
                    if chk(r, c, i):
                        q.append((r + dy[i], c + dx[i], cnt + 1))
                        arr[r + dy[i]][c + dx[i]] = 1
    print(-1)
    return
dy = [-3, -2, 2, 3, 3, 2, -2, -3]
dx = [2, 3, 3, 2, -2, -3, -3, -2]

arr = [[0]*9 for _ in range(10)]
R1, C1 = map(int, input().split())
R2, C2 = map(int, input().split())

q = []
BFS(R1, C1, 0)