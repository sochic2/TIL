import sys
sys.stdin = open('반나누기.txt')
T = int(input())

for tc in range(1, T+1):
    N, K_Min, K_Max = map(int, input().split())
    data = list(map(int, input().split()))
    score = set(sorted(data))
    score = list(score)
    # print(N, K_Min, K_Max)
    # print(data)
    # print(score)
    #
    different = 987654321

    for i in range(len(score)-1):
        for j in range(i+1, len(score)):
            class_room = [0] * 3
            T1 = score[i]
            T2 = score[j]
            # print(T1, T2)
            for k in range(len(data)):
                if data[k] < T1:
                    class_room[2] += 1
                if data[k] >= T1 and data[k] < T2:
                    class_room[1] += 1
                if data[k] >= T2:
                    class_room[0] += 1
            if min(class_room) >= K_Min and max(class_room) <= K_Max:
                if max(class_room) - min(class_room) < different:
                    different = max(class_room) - min(class_room)
    if different == 987654321:
        print(-1)
    else:
        print(different)



