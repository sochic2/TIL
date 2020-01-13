n, k = 3, 5
def solution(n, k):
    answer = []
    nums = [range(1, n+1)]
    fact = 1
    for i in range(1, n):
        fact *= i


    while True:
        answer.append(nums.pop(k//fact))
        fact = fact//k + fact




    return solution[0]

print(solution(n, k))