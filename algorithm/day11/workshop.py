import sys
sys.stdin = open('행렬찾기_input.txt')

def find(data):
    result = []

    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] != 0:
                p = i
                result += [[]]
                cnt = 0
                while data[p][j] !=0:

                    result[-1].append(data[p][j])
                    data[p][j] = 0
                    p += 1
                    cnt += 1
                result.append(cnt)
    return print(result)


    # print(result)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    data = []
    for i in range(n):
        data += [list(map(int, input().split()))]
    # print(n, data)
    find(data)
