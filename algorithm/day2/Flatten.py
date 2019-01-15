import sys
sys.stdin = open("flatten_input.txt")
T = 10
for n in range(1, 11):
    N = int(input())
    data = list(map(int, input().split()))



    for i in range(N):
        for i in range(len(data) - 1, 0, -1):
            for j in range(i):
                if data[j] < data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        data[0] += -1
        data[-1] += 1
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    max_num = data[0]
    min_num = data[-1]
    result = max_num - min_num
    print(f'#{n} {result}')

