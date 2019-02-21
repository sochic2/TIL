import sys
sys.stdin = open('토너먼트카드게임_input.txt')


def winner(data):
    if len(data) - data.count(0) > 2:
        return winner(winner(data[:(len(data) + 1) // 2]) + winner(data[(len(data) + 1) // 2:]))
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

    result = winner(data)
    for i in range(len(result)):
        if result[i]:
            print(f'#{tc+1} {i+1}')

        
