import sys
sys.stdin = open('피자_input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    cheese.insert(0, 0)

    oven = [_ for _ in range(1, N+1)]

    Z = N
    # print(oven)
    # print(cheese)

    while oven.count(0) != N-1:
        if oven[0] != 0:
            if cheese[oven[0]] != 0:
                if cheese[oven[0]]//2 != 0:
                    cheese[oven[0]] = cheese[oven[0]]//2
                    oven.append(oven.pop(0))
                else:
                    cheese[oven[0]] = cheese[oven[0]] // 2
                    oven.pop(0)

                    if Z + 1 <= M:
                        Z += 1
                        oven.append(Z)
                    else:
                        oven.append(0)

            else:
              oven.append(oven.pop(0))
        else:
            oven.append(oven.pop(0))

    for i in oven:
        if i != 0:
            print('#{} {}'.format(tc, i))


