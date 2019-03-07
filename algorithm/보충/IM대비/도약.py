import sys
sys.stdin = open('도약.txt')
N = int(input())
lake = []
for i in range(N):
    lake += [int(input())]
lake.sort()

solution = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1,N):
            if (lake[j] - lake[i]) * 2 >= lake[k]-lake[j] and lake[j] - lake[i] <=lake[k]-lake[j] :
                solution +=1
print(solution)

