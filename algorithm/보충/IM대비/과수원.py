import sys
sys.stdin = open('과수원.txt')
N = int(input())
data = [list(map(int, input())) for _ in range(N)]
count = 0
solution = 0
for i in range(N-1):
    for j in range(1, N):
        part_1 = []
        part_2 = []
        part_3 = []
        part_4 = []
        for k in range(i+1):
            part_1 += data[k][:j]
            part_2 += data[k][j:]

        for l in range(i+1, N):
            part_3 += data[l][:j]
            part_4 += data[l][j:]
        count += 1
 
        if sum(part_1) == sum(part_2) == sum(part_3) == sum(part_4):
            solution += 1

if solution == 0:
    print(-1)
else:
    print(solution)