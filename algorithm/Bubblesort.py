# def bubblesort(data):
#     for i in range(len(data)-1, 0, -1):      #4, 3, 2, 1 순으로 들어오는거
#         for j in range(0, i):                #4번 3번 2번 1번
#             if data[j] < data[j+1]:
#                 data[j], data[j+1] = data[j+1], data[j]


data = [55, 7, 78, 12, 42]
# bubblesort(data)
data.sort()
print(data)

