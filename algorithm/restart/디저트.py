import sys
sys.stdin = open('디저트.txt')

def check():
    global N
    dy = [1, 1, -1, -1]
    dx = [-1, 1, 1, -1]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maparr = [list(map(int, input().split())) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            visit = [0] * 100
            check(y, x, 4)
