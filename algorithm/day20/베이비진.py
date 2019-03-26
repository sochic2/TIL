import sys
sys.stdin = open('베이비진게임.txt')

T = int(input())

for tc in range(1, T+1):
    data = list(map(int, input().split()))
    a = []
    b = []
    flag = 0
    solution = 0
    for i in range(12):
        if flag == 1:
            break
        else:
            if i % 2:
                b.append(data[i])
                b.sort()
                b_set = list(set(b))
                b_set.sort()
                if len(b) >= 3:
                    for k in range(len(b)-2):
                        if b[k] == b[k+1] and b[k+1] == b[k+2]:
                            solution = 2
                            flag = 1
                if len(b_set) >= 3:
                    for k in range(len(b_set)-2):
                        if b_set[k] == b_set[k+1] -1 and b_set[k+1] == b_set[k+2] -1:
                            solution = 2
                            flag = 1
            else:
                a.append(data[i])
                a.sort()
                a_set = list(set(a))
                a_set.sort()
                if len(a) >= 3:
                    for k in range(len(a)-2):
                        if a[k] == a[k+1] and a[k+1] == a[k+2]:
                            solution = 1
                            flag = 1
                if len(a_set) >= 3:
                    for k in range(len(a_set)-2):
                        if a_set[k] == a_set[k+1] -1 and a_set[k+1] == a_set[k+2] -1:
                            solution = 1
                            flag = 1


    print('#{} {}'.format(tc, solution))
