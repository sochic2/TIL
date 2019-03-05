import sys
sys.stdin = open('사칙연산.txt')
T = 10
for tc in range(1, T+1):
    N = int(input())
    numbers = [0] * (N+1)
    op = [''] * (N+1)
    l_child = [0] * (N + 1)
    r_child = [0] * (N+1)

    for _ in range(N):
        a = list(map(''.join, input().split()))

        if len(a) == 4:
            op[int(a[0])] = a[1]
            l_child[int(a[0])] = int(a[2])
            r_child[int(a[0])] = int(a[3])

        elif len(a) == 2:
            numbers[int(a[0])] = int(a[1])

    # print(numbers)
    # print(op)
    # print(l_child)
    # print(r_child)

    while numbers[1] == 0:
        for i in range(N, 0, -1):
            if r_child[i] != 0:
                if op[i] == '-':
                   numbers[i] = numbers[l_child[i]] - numbers[r_child[i]]
                if op[i] == '+':
                    numbers[i] = numbers[l_child[i]] + numbers[r_child[i]]
                if op[i] == '*':
                    numbers[i] = numbers[l_child[i]] * numbers[r_child[i]]
                if op[i] == '/':
                    numbers[i] = numbers[l_child[i]] // numbers[r_child[i]]



    print('#{} {}'.format(tc, numbers[1]))

