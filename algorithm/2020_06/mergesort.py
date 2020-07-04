# def merge_sort(arr):
#     if len(arr) < 2:
#         return arr
#
#     mid = len(arr) // 2
#     low_arr = merge_sort(arr[:mid])
#     high_arr = merge_sort(arr[mid:])
#
#     merged_arr = []
#     l = h = 0
#     while l < len(low_arr) and h < len(high_arr):
#         if low_arr[l] < high_arr[h]:
#             merged_arr.append(low_arr[l])
#             l += 1
#         else:
#             merged_arr.append(high_arr[h])
#             h += 1
#     merged_arr += low_arr[l:]
#     merged_arr += high_arr[h:]
#     return merged_arr


# print(merge_sort([7, 1, 2, 4, 5]))

#
# def merge_sort_2(arr):
#     def sort(low, high):
#         if high - low < 2:
#             return
#         mid = (low + high) // 2
#         sort(low, mid)
#         sort(mid, high)
#         merge(low, mid, high)
#
#     def merge(low, mid, high):
#         temp = []
#         l, h = low, mid
#
#         while l < mid and h < high:
#             if arr[l] < arr[h]:
#                 temp.append(arr[l])
#                 l += 1
#             else:
#                 temp.append(arr[h])
#                 h += 1
#
#         while l < mid:
#             temp.append(arr[l])
#             l += 1
#         while h < high:
#             temp.append(arr[h])
#             h += 1
#
#         for i in range(low, high):
#             arr[i] = temp[i - low]
#
#     return sort(0, len(arr))
#
#
# arr = merge_sort_2([7, 1, 2, 4, 5])
# print(arr)


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    #둘중 한군데 끝나면 진행한곳 이후는 슬라이싱해서 한번에 넣기 어차피 크기비교 된거니깐 이전에.
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


print(merge_sort([7, 1, 2, 4, 5]))
#홀