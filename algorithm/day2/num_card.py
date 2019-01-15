import sys
sys.stdin = open("num_card_sample_input.txt")
T = int(input())
for tc in range(T):
    ans = 0
    N = int(input())
    data = list(input())
    cnt = [0] * 10
    # print(data)   #걍 숫자를 하나씩 받는게 편할듯..?

    int_data = []
    maximum = 0


    for i in range(len(data)):
        int_data += [int(data[i])]
    # print(int_data)

    for i in range(len(int_data) - 1, 0, -1):
        for j in range(0, i):
            if int_data[j] > int_data[j + 1]:
                int_data[j], int_data[j + 1] = int_data[j + 1], int_data[j]
    # print(int_data)

    for i in range(len(int_data)):
        cnt[int_data[i]] += 1
    # print(cnt)

    for i in range(len(cnt)):
        if maximum <= cnt[i]:
            maximum, cnt[i] = cnt[i], maximum
            idx = i

    print("#{} {} {}".format(tc + 1, idx, maximum))