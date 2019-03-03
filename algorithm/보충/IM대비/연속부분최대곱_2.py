import sys
sys.stdin = open('연속부분최대곱.txt')

N = int(input())
numbers = [float(input()) for _ in range(N)]

maxN = 0
for i in range(N-1, -1, -1):
    if numbers[i] >= 1:
        mul, j = 1, i
        while j > -1:
            if not numbers[j]:
                break
            mul *= numbers[j]
            j -= 1
            if maxN < mul:
                maxN = mul
if maxN == 0:
    maxN = max(numbers)

print(format(maxN, '.3f'))
