def sequentisalSearch(a, n, key):
    i = 0
    while i< n and a[i] != key:
        i = i+1
    if i < n : return i
    else: return -1

# for문 써서 하는거
#     for i in range(n):
#         if a[i] == key:
#             return i
#     return -1
#
#

data = [4, 9, 11, 23, 2, 7, 19]
key = 19
print(sequentisalSearch(data, len(data), key))

    