total = 0
N = 10
A = [0 for _ in range(N)]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def printSet(n):

    ssum = 0

    for i in range(n):

        if A[i] == 1:
            ssum += data[i]

    if ssum == 10:
        for i in range(n):
            if A[i] == 1:
                print('{} '.format(data[i]), end="")
        print()

def powerset(n, k):
    global total

    ssum = 0
    for i in range(n):
        if A[i] == 1:
            ssum += data[i]
    if ssum > 10:
        return
    total += 1



    if n == k:
        printSet(n)
    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)

powerset(N, 0)
print('total', total)