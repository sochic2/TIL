def DFS2(no, ssum, size, ssum_B):
    global solution, N
    if no >= N:
        if ssum + ssum_B > solution:
            solution = ssum + ssum_B
    else:
        if arr[no] == 0 and size > boxes[no]:
            DFS2(no+1, ssum, size, ssum_B)
            arr[no] = 1
            DFS2(no+1, ssum + boxes[no], boxes[no], ssum_B)
            arr[no] = 0
        else:
            DFS2(no+1, ssum, size, ssum_B)

def DFS(no, ssum, size):
    if no >= N:
        DFS2(0, 0, 1001, ssum)
    else:
        if arr[no] == 0 and size < boxes[no]:
            DFS(no+1, ssum, size)
            arr[no] = 1
            DFS(no+1, ssum + boxes[no], boxes[no])
            arr[no] = 0

        else:
            DFS(no+1, ssum, size)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))
    arr = [0] * N
    solution = 0
    DFS(0, 0, 0)

    print(solution)