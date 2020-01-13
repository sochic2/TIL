def solution(n, times):

    mn = 0
    mx = n * max(times)
    temp = mx
    answer = mx
    while mx>=mn:
        mid = (mn + mx) // 2
        people = 0
        for i in times:
            people += mid//i
        if people == n:
            if answer >= mid:
                answer = mid
            mx = mid-1
        elif people>n:
            mx = mid-1
        else:
            mn = mid+1
    if answer == temp:
        return mx+1
    else:
        return answer



solution()