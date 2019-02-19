import sys
sys.stdin = open('토너먼트카드게임_input.txt')


def winner(data):

    if len(data) - data.count(0) > 2:
        winner(data[:(len(data)+1)//2])
        winner(data[(len(data)+1)//2:])
    elif len(data) - data.count(0) == 2:
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





T = int(input())
for tc in range(T):
    N = int(input())
    dataA = list(map(int, input().split()))


    print(winner(data))