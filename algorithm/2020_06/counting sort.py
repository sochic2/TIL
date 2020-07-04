def countingSort(A, smallest, largest):
    nbins = largest - smallest + 1  # 이만큼의 공간안에 숫자들이 다 들어갈 것입니다.
    bins = [0] * nbins  # bins라는 공간에 할당해 놓고,
    # 각 원소를 count합니다.
    for i in A:
        bins[i - smallest] += 1

    # 마지막으로 count된 횟수만큼씩 그대로 넣어주면 정렬이 될 것입니다.
    index = 0
    for i in range(nbins):
        for j in range(bins[i]):
            A[index] = i + smallest
            index += 1

A = [7, 1, 1, 2, 4, 5]
print(countingSort(A, 1, 7))
print(A)







def countingsort(A, B, C):
    for i in range(len(A)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1


A = [1, 4, 5, 1, 2, 4, 5, 7, 9, 3]
B = [0] * len(A)
C = [0] * (max(A)+1)
countingsort(A, B, C)
print(B)


def counting_sort(array, max):
    # counting array 생성
    counting_array = [0] * (max + 1)

    # counting array에 input array내 원소의 빈도수 담기
    for i in array:
        counting_array[i] += 1

    # counting array 업데이트.
    for i in range(max):
        counting_array[i + 1] += counting_array[i]

    # output array 생성
    output_array = [-1] * len(array)

    # output array에 정렬하기(counting array를 참조)
    for i in reversed(array):
        a = counting_array[i]
        output_array[counting_array[i] - 1] = i
        counting_array[i] -= 1
    return output_array

A = [1, 4, 5, 1, 2, 4, 5, 7, 9, 3]
B = counting_sort(A, max(A))
print(B)