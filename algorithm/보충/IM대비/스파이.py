import sys
sys.stdin = open('스파이.txt')
N, T = input().split()
N = int(N)
data = []
for i in T:
    data.append(i)
# print(data)

stack = ''
data_1 = []
for j in data:
    if j != '>' and j != '<':
        stack += j

    elif j == '>' and stack:
        data_1 += [stack]
        stack = ''
        data_1 += [j]

    elif j == '<' and stack:
        data_1 += [stack]
        stack = ''
        data_1 += [j]

    else:
        data_1 += [j]
# print(data_1)

result = [[] for _ in range(51)]

cnt = 0
for i in data_1:
    if i != '<' and i != '>':
        result[cnt].append(i)

    elif i == '<':
        cnt += 1
    elif i == '>':
        cnt -= 1
# print(result)
print(*result[N])