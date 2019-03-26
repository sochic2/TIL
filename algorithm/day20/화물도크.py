import sys
sys.stdin = open('화물도크.txt')
def ssum(p_s):
    global result
    solution = 0
    for i in range(len(p_s)-1):
        if p_s[i][1] > p_s[i+1][0]:
            return
        else:
            solution += 1
    if solution > result:
        result = solution

def powerset(n, k):
    global result
    flag = 0
    if A.count(1) >= 2:
        for i in range(N-1, 0, -1):
            if flag == 1:
                break

            if A[i] == 1:
                t = i
                flag = 0
                while flag != 1:
                    t -= 1
                    if A[t] == 1:
                        if data[t][1] > data[i][0]:
                            return
                        elif data[t][1] <= data[i][0]:
                            flag = 1
    if n == k:
        if A.count(1) <= result:
            return
        p_s = []
        for i in range(N):
            if A[i] == 1:
                p_s.append(data[i])
        # print(A)
        ssum(p_s)
    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort()
    # print(data)
    A = [0] * (N)
    # print(A)
    result = 0
    powerset(N, 0)
    print('#{} {}'.format(tc, result+1))












