N = 2
number = 11


def solution(N, number):
    def make_number(cnt, num, arr):
        if num >= 32000:
            return
        if num > 0:
            if arr[num] < cnt or cnt > 9:
                return
            if arr[num] > cnt:
                arr[num] = cnt

        for i in range(1, 10 - cnt):
            new_num = int(str(N) * i)
            make_number(cnt + i, num * new_num, arr)
            make_number(cnt + i, num + new_num, arr)
            make_number(cnt + i, num - new_num, arr)
            make_number(cnt + i, num // new_num, arr)

    answer = -1
    arr = [987654321] * 34000
    arr[N] = 1
    make_number(1, 0, arr)
    if arr[number] != 987654321:
        answer = arr[number] - 1

    return answer


print(solution(2, 11))


