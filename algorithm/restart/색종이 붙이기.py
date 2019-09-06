import sys
sys.stdin = open('색종이 붙이기.txt')

def clean(y, x, i):
    for nny in range(y, y+i):
        for nnx in range(x, x+i):
            arr[nny][nnx] = 0

def restore(y, x, i):
    for nny in range(y, y+i):
        for nnx in range(x, x+i):
            arr[nny][nnx] = 1

def find(y, x, i):
    for nny in range(y, y+i):
        for nnx in range(x, x+i):
            if arr[nny][nnx] == 0:
                return 0
    return 1

def start(n):
    global mmin
    if n >= mmin:
        return
    for y in range(10):
        for x in range(10):
            if arr[y][x] == 1:
                for i in range(5, 0, -1):
                    if paper[i] <= 0: continue
                    if y+i > 10 or x +i > 10: continue
                    flag = find(y, x, i)
                    if flag == 1:
                        clean(y, x, i)
                        paper[i] -= 1
                        start(n+1)
                        paper[i] += 1
                        restore(y, x, i)
                return


    for y in range(10):
        for x in range(10):
            if arr[y][x]:
                return

    if n <= mmin:
        mmin = n

arr = [list(map(int, input().split())) for _ in range(10)]
mmin = 987654321
paper = [0, 5, 5, 5, 5, 5]
start(0)
if mmin == 987654321:
    print(-1)
else:
    print(mmin)