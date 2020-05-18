


def solution(numbers, hand):
    answer = ''
    l = [1, 4, 7]
    r = [3, 6, 9]
    location = [10, 12]
    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = 11
        if numbers[i] in l:
            answer += 'L'
            location[0] = numbers[i]
        elif numbers[i] in r:
            answer += 'R'
            location[1] = numbers[i]
        else:
            rd = abs(location[1] - numbers[i]) // 3 + abs(location[1] - numbers[i]) %3
            ld = abs(location[0] - numbers[i]) // 3 + abs(location[0] - numbers[i]) %3
            if rd < ld:
                answer += 'R'
                location[1] = numbers[i]
            elif rd > ld:
                answer += 'L'
                location[0] = numbers[i]
            else:
                if hand == 'right':
                    answer += 'R'
                    location[1] = numbers[i]
                else:
                    answer += 'L'
                    location[0] = numbers[i]



    return answer



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"

print(solution(numbers, hand))