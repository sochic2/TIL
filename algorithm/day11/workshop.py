import sys
sys.stdin = open('행렬찾기_input.txt')


def find(data):
    result = []

    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] != 0:
                p = i
                result += [[]]

                while data[p][j] != 0:
                    result[-1].append(data[p][j])
                    data[p][j] = 0
                    p += 1

    return result

    # print(result)


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    data = []
    for i in range(n):
        data += [list(map(int, input().split()))]
    # print(n, data)
    change_data = (find(data))
    result_2 = []

    for i in change_data:
        if len(i) not in result_2:
            result_2 += [len(i)]
    result_3 = [0] * len(result_2)

    for j in range(len(result_2)):
        for k in change_data:
            if result_2[j] == len(k):
                result_3[j] += 1

    final_result = []

    for o in range(len(result_2)):
        final_result += [[result_2[o], result_3[o]]]

    for p in final_result:
        p.insert(0, p[0] * p[1])

    final_result.sort()

    print(f'#{tc} {len(final_result)}', end=' ')
    for z in final_result:
        print(z[1], z[2], end=' ')

    print()