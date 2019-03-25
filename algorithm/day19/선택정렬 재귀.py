def SelectionSort(A):
    n = len(A)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if A[j] < A[min]:
                min = j
        temp = A[min]
        A[min] = A[i]
        A[i] = temp

def recselectionsort(ary, s, e):
    mini = s
    if s == e: return
    for j in range(s+1, e, 1):
        if ary[j] < ary[mini]:
            mini = j
    ary[s], ary[mini] = ary[mini], ary[s]
    recselectionsort(ary, s+1, e)

A = [5, 2, 6, 1, 10]
B = [ 5, 2, 7, 1, 3, 8, 9, 3, 5, 2]
SelectionSort(A)
print(A)
recselectionsort(B, 0, 10)
print(B)