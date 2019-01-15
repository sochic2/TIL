import sys
sys.stdin = open("min_max_sample_input.txt")
T = int(input())
for tc in range(T):
    ans = 0
    N = int(input())
    data = list(map(int, input().split()))
    # print(data)


    for i in range(len(data)-1, 0, -1):
        for j in range(0, i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                ans = data[-1] - data[0]


    print("#{} {}".format(tc+1, ans))

