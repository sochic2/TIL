arr = [-7, -3, -2, 5, 8]
n = len(arr)


for i in range(1 << n):
# 위에거랑 이거랑 같음
# for i in range(2 ** len(arr)):
    sum = 0
    for j in range(n+1):
        if i & (1<<j):
            sum += arr[j]


    if sum == 0:

        for j in range(len(arr)):
            if i & (1<<j):
                print(arr[j], end = " ")
        print()


