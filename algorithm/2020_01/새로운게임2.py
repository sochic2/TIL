
def go():


N, K = map(int, input().split())
marr = [list(map(int, input().split())) for _ in range(N)]
knights = [tuple(map(int, input().split())) for _ in range(K)]

print(marr)

t = 0
while True:
    if t >= 1001:
        print(-1)
    if go():
        print(t)
        break