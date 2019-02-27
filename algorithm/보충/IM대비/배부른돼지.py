n = int(input())
data = []
for i in range(n):
    data += [input().split()]
# print(data)


def happy(n):
    happy = 200
    for i in range(len(data)):
        if data[i][1] == 'Y':

            if int(data[i][0]) < happy:
                happy = int(data[i][0])

        elif happy != 200 and data[i][1] == 'N':
            if int(data[i][0]) > happy:
                return print('F')

    if happy == 200:
        return print('F')
    else:
        return print(happy)

happy(n)

# N의 최댓값고 Y의 최솟값 구해서 비교해서 모순인지 아닌지 구분하는 법으로
# 다시 짜볼것