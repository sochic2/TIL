def binSearch(s, e, data):
    # data가 mid번째 값이면 mid위치 +1 리턴
    # data가 mid번째값보다 크면 오른쪽영역 재탐색
    # data가 mid번째보다 작으면 왼쪽영역 재탐색
    while s <= e:
        mid = (s + e) // 2
        if data == arr[mid] : return mid+1
        if data > arr[mid] : s = mid+1
        else: e = mid-1


    return 0

N = int(input())
arr = list(map(int, input().split()))
T = int(input())
Tarr = list(map(int, input().split()))

for i in range(T):
    print(binSearch(0, N-1, Tarr[i]))
