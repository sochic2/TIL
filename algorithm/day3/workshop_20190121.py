import sys
sys.stdin = open("homework_input.txt")
T = 10
# arr = [[0 for _ in range(5)] for _ in range(5)]
#                 #열,                 행
# print(arr)
#
# for i in range(5):
#     arr[i] = list(map(int, input().split()))

arr = [[0 for _  in range(100)]for _ in range(100)]

for i in range(T):
    N = input()
    for j in range(100):
        arr[j] = list(map(int, input().split()))
# print(arr)
    yt, xt = 0, 0
    for x in range(100):
        sum_y = 0
        for y in range(100):
            sum_y += arr[x][y]
        if sum_y > yt:
            yt = sum_y
    for x in range(100):
        sum_x = 0
        for y in range(100):
            sum_x += arr[y][x]
        if sum_x > xt:
            xt =sum_x
    sum_rd = 0
    for x in range(100):
        sum_rd += arr[x][x]
    sum_ld = 0
    for x in range(100):
        sum_ld += arr[x][99-x]



    result = max(yt, xt, sum_rd, sum_ld)
    print("#{} {}".format(i + 1, result))