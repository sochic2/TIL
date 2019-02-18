import sys
sys.stdin = open('workshop_input.txt')
T = 10
for tc in range(T):
    x = int(input())
    # print(x)
    data = [[] for _ in range(x)]


    for i in range(x):
        a = list(map(int, input().split()))
        for j in range(x):
            data[j] += [a[j]]



    for k in range(x):
        for o in range(x):
            if data[k][o] == 1:
                break
            else:
                data[k][o] = 0

    for p in range(x):
        for q in range(x):
            if data[p][-1-q] == 2:
                break
            else:
                data[p][-1-q] = 0

    print(data)
    result = 0






    # print(f'{tc+1}, {result}')

