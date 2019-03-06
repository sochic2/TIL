import sys
sys.stdin = open('회전초밥.txt')

N, d, k, c = map(int, input().split())
print(N, d, k, c)
belt = []

for _ in range(N):
    belt += [int(input())]

print(belt)

