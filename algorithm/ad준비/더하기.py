import sys
sys.stdin = open('더하기.txt')

def DFS(no, ssum):
    global flag, N, K
    if flag or ssum > K: return

    if no >= N:
        if ssum == K:
            flag = 1
        return

    DFS(no+1, ssum + di_arr[no])
    DFS(no+1, ssum)



T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())   # 갯수 N, 합 K
    di_arr = list(map(int, input().split()))

    flag = 0
    DFS(0,0)
    if flag :
        print('YES')
    else:
        print('NO')
