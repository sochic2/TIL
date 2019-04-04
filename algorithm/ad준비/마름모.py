N, K = map(int, input().split())
data = list(input())
div = N//4
solution = []
six = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
for i in range(N):
    data.append(data.pop(0))
    # print(data)
    for j in range(4):
        result = []
        result_2 = 0
        for k in range(div):
            result.append(data[j*div + k])
        # for z in result:
        result.reverse()
        for z in range(len(result)):
            for x in range(len(six)):
                if six[x] == result[z]:
                    result_2 += x * 16 ** z
        if result_2 not in solution:
            solution += [result_2]
solution.sort(reverse=True)
print(solution[K-1])
