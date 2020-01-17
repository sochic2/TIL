distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2


def solution(distance, rocks, n):
    answer = []
    rocks.append(distance)
    rocks.sort()

    left = 1
    right = distance

    while right >= left:
        mid = (left + right)//2
        if mid in answer:break
        if check(n, mid, rocks, answer):
            left = mid + 1
        else:
            right = mid-1

    return max(answer)

def check(n, mid, rocks, answer):
    mmin = 987654321
    start = 0
    for i in range(len(rocks)):
        if n < 0:return False
        if rocks[i] - start < mid:
            if n > 0 :
                n-= 1
            else:
                return False
        else:
            if mmin > rocks[i] - start:
                mmin = rocks[i] - start
            start = rocks[i]

    answer.append(mmin)
    return True




print(solution(distance, rocks, n))