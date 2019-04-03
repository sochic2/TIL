def clear(no):
    for i in range(N):
        temp = abs(arr[no][1] - arr[i][1]) + abs(arr[no][0] - arr[i][0])
        if  temp <= R:
            arr[i][2] -= P
def update(no):
    for i in range(N):
        temp = abs(arr[no][1] - arr[i][1]) + abs(arr[no][0] - arr[i][0])
        if temp <= R:
            arr[i][2] += P


def DFS(no):
    global sol, count
    if no == M:
        # count += 1
        cnt = 0   # 남아있는 군함의 개수
        for i in range(N):
            if arr[i][2] > 0: cnt += 1
        if cnt < sol:
            sol = cnt
        return

    for i in range(N):
        if arr[i][2] <= 0 : continue
        clear(i) # 현재 군함 반경이내 모든 군함에너지 차감
        DFS(no + 1)
        update(i)


N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
M, P, R = map(int, input().split())
count = 0
sol = 16
DFS(0)
print(sol)
# print(count)