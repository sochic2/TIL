import sys
sys.stdin = open('디저트.txt')
def check(y, x, yy, xx):
    result = []
    dy = [1, 1, -1, -1]
    dx = [-1, 1, 1, -1]
    for py in range(yy):

    for px in range(xx):

    for py in range(yy):

    for px in range(xx):


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maparr = [list(map(int, input().split())) for _ in range(N)]
    mmax = -1
    for y in range(N):
        for x in range(N):
            for yy in range(N-1):
                for xx in range(N-1):
                    check(y, x, yy, xx)