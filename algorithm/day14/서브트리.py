import sys
sys.stdin = open('서브트리.txt')
T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))

    count = 0
    stack = [N]
    while len(stack) > 0:

        a = stack.pop(0)
        for i in range(E*2):
            if i % 2 == 0  and data[i] == a:
                count += 1
                stack.append(data[i+1])

    print('#{} {}'.format(tc, count+1))




