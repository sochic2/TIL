import sys
sys.stdin = open('최대상금.txt')
T = int(input())
def bonus(change):
    global solution
    if change == 0:
        if int(''.join(a)) > solution:
            solution = int(''.join(a))
            return
    else:
        for i in range(len(a)-1):
            for j in range(i+1, len(a)):
                if a[i] == a[j]:

                    if change == 1:
                        if int(''.join(a)) > solution:
                            solution = int(''.join(a))

                    else:
                        change -= 1


                else:
                    a[i], a[j] = a[j], a[i]
                    bonus(change-1)
                    a[i], a[j] = a[j], a[i]





for tc in range(1, T+1):
    a, change = map(str, input().split())
    a = list(a)
    change = int(change)
    solution = 0
    if change > len(a):
        change = len(a)
    bonus(change)

    print('#{} {}'.format(tc, solution))