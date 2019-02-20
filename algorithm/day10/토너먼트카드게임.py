import sys
sys.stdin = open('토너먼트카드게임_input.txt')


def winner(data):
    if len(data) - data.count(0) > 2:
        return winner(data[:(len(data) + 1) // 2]) + winner(data[(len(data) + 1) // 2:])
    if len(data) - data.count(0) == 2:
        a = []
        for idx, value in enumerate(data):
            if a == [] and value != 0:
                a += [idx, value]
            elif len(a) == 2 and value != 0:
                if a[1] == value:
                    data[idx] = 0
                elif a[1] == 1:
                    if value == 2:
                        data[a[0]] = 0
                    elif value == 3:
                        data[idx] = 0
                elif a[1] == 2:
                    if value == 3:
                        data[a[0]] = 0
                    elif value == 1:
                        data[idx] = 0
                elif a[1] == 3:
                    if value == 1:
                        data[a[0]] = 0
                    elif value == 2:
                        data[idx] = 0
    return data


T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    # print(winner(data))
    a = winner(data)

    while a.count(0) != N - 1 or b.count(0) != N - 1:
        b = winner(a)
        a = winner(b)
    result = 0
    for i in range(len(a)):
        if a[i] != 0:
            result = i + 1

    print(f'#{tc + 1} {result}')