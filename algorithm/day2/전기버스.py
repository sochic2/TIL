import sys
sys.stdin = open("전기버스_input.txt")
# T = int(input())
# for tc in range(T):
#     ans = 0
#     k, n, m = map(int, input().split())
#     data = list(map(int, input().split()))
#     charge = [0] * (n+1)
#     stop = [0] * (n+1)
#     stop[0] = k
#     # print(data)
#     k_list = [0]*k
#
#     for i in range(len(data)):
#         charge[(data[i])] = 1
#     print(charge)
#
#     for i in range(1, len(charge)):
#
#         if charge[i] == 0:
#             stop[i] = stop[i-1] -1
#         if charge[i] == 1:
#             stop[i] = k
#         if stop[i] < 1:
#             ans = 0
#             break
#     print(stop)
    # for i in range(len(stop)-k-1):
    #     for j in range():
    #         k_list += [stop[j]]
    # print(k_list)


    # k -= 1

# import sys
# sys.stdin = open("bus_input.txt")

T = int(input())

for n in range(1, T + 1):
    K, N, M = map(int, input().split())
    route = list(map(int, input().split()))
    charge_route = [0] * (N+1)
    charge_route[N] = 1

    for i in route:
        charge_route[i] = 1
    count = 0
    point = K

    while True:
        if charge_route[point] != 1:
            point += -1
        elif charge_route[point] == 1:
            count += 1
            charge_route = charge_route[point:]
            point = K
            if len(charge_route) <= K:
                # count += -1
                break

        if point == 0:
            count = 0
            break
    print(f'#{n} {count}')
