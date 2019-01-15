import sys
sys.stdin = open("전기버스_input.txt")
T = int(input())
for tc in range(T):
    ans = 0
    k, n, m = map(int, input().split())
    data = list(map(int, input().split()))
    charge = [0] * (n+1)
    stop = [0] * (n+1)
    stop[0] = k
    # print(data)
    k_list = [0]*k

    for i in range(len(data)):
        charge[(data[i])] = 1
    print(charge)

    for i in range(1, len(charge)):

        if charge[i] == 0:
            stop[i] = stop[i-1] -1
        if charge[i] == 1:
            stop[i] = k
        if stop[i] < 1:
            ans = 0
            break
    print(stop)
    # for i in range(len(stop)-k-1):
    #     for j in range():
    #         k_list += [stop[j]]
    # print(k_list)


    # k -= 1