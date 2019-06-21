import sys
sys.stdin = open("grade.txt")
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort()
    score.reverse()
    print("#{} {}".format(tc, sum(score[:K])))

