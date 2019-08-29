import sys
sys.stdin = open('p1.txt')
def check(arr, cnt):
    global N, mmin
    if cnt > 5:
        return
    if cnt != 0:
        if arr == cardarr:
            return
    if cnt >= mmin:
        return
    if arr == sorted(arr) or arr == sorted(arr, reverse=True):
        if cnt <= mmin:
            mmin = cnt

    else:
        shuffle(arr, cnt)

def shuffle(arr, cnt):

    for i in range(N):
        newarr = []
        leftarr = arr[0:N // 2]
        rightarr = arr[N // 2:N]
        if i < N//2:
            for j in range(N//2 - i):
                newarr.append(leftarr.pop(0))

            while len(rightarr) != 0:
                if len(leftarr) == 0:
                    newarr.append(rightarr.pop(0))
                else:
                    newarr.append(rightarr.pop(0))
                    newarr.append(leftarr.pop(0))


        else:
            for j in range(i-N//2+1):
                newarr.append(rightarr.pop(0))

            while len(leftarr) != 0:
                if len(rightarr) == 0:
                    newarr.append(leftarr.pop(0))
                else:
                    newarr.append(leftarr.pop(0))
                    newarr.append(rightarr.pop(0))

        check(newarr, cnt+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cardarr = list(map(int, input().split()))
    mmin = 987654321

    check(cardarr, 0)
    if mmin == 987654321:
        mmin = -1
    print('#{} {}'.format(tc, mmin))