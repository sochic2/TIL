import sys
sys.stdin = open("구간합_input.txt")
T = int(input())
for tc in range(T):
    ans = 0
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    maximum = -987654321
    minimum = 987654321



    for i in range(len(data)-(m-1)):
        plus_data = 0
        plus_data_2 = 0
        for j in range(i, i+m):
            plus_data += data[j]
            plus_data_2 += data[j]

        if maximum < plus_data:
            maximum, plus_data = plus_data, maximum

        if minimum > plus_data_2:
            minimum, plus_data_2 = plus_data_2, minimum

    print("#{} {}".format(tc + 1, maximum-minimum))



