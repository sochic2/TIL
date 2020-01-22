left = [3, 2, 5]
right = [2, 4, 1]


def solution(left, right):
    answer = 0
    mmax = -987654321
    visit = [[0] * (len(left)+1) for _ in range(len(left)+1)]

    for l in range(1, len(left)+1):
        for r in range(1, len(right)+1):
            visit[l][r] = max(visit[l-1][r-1], visit[l-1][r])
            if left[l-1] > right[r-1]:
                visit[l][r] = visit[l][r-1] + right[r-1]

    print(visit)
    return visit[len(left)][len(right)]

print(solution(left, right))

#
#


# def solution(left, right):
#     dp = [[0 for x in range(len(left)+1)] for y in range(len(right)+1)]
#     for i in range(1, len(left)+1):
#         for j in range(1, len(right)+1):
#             dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
#             if right[j-1] < left[i-1]:
#                 dp[i][j] = dp[i][j-1] + right[j-1]
#     print(dp)
#     return dp[len(left)][len(right)]
#
#
# print(solution(left, right))