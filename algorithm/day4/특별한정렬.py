import sys
sys.stdin = open("특별한정렬_input.txt")
T = int(input())
def sel_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    # print(N)
    # print(data)
    sel_sort(data)
    result = []
    for k in range(5):
        result += data[-1-k], data[k]
    print(f'#{tc + 1}', *result)




