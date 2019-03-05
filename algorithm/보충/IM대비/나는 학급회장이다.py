import sys
sys.stdin = open('학급회장.txt')

N = int(input())

candidate = [[],[],[]]


for _ in range(N):
    data = list(map(int, input().split()))
    candidate[2].append(data.pop())
    candidate[1].append(data.pop())
    candidate[0].append(data.pop())


change_candidate = [[sum(candidate[0]), candidate[0].count(3), candidate[0].count(2)], [sum(candidate[1]), candidate[1].count(3), candidate[1].count(2)], [sum(candidate[2]), candidate[2].count(3), candidate[2].count(2)]]












