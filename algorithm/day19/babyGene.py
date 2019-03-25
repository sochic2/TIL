

arr= [1, 2, 4, 7, 8, 3]
# arr = [0, 5, 4, 0, 6, 0]
def perm(n, k):
    global flag
    if k == n :
        result = 0
        if arr[0] == arr[1] and arr[1] == arr[2]:
            result += 1
        if arr[3] == arr[4] and arr[4] == arr[5]:
            result += 1
        if arr[0]+1 == arr[1] and arr[1] + 1 == arr[2]:
            result += 1
        if arr[3]+1 == arr[4] and arr[4] + 1 == arr[5]:
            result += 1

        if result >= 2:
            flag = 1

    else:

        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k+1)
            arr[i], arr[k] = arr[k], arr[i]

flag = 0
perm(6, 0)


if flag == 1:
    print('딩동댕')
else:
    print('땡')

