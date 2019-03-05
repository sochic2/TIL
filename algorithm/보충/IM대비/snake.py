import sys
sys.stdin = open('snake.txt')

N = int(input())
K = int(input())
fruite = []
for _ in range(K):
    fruite.append(list(map(int, input().split())))

L = int(input())

direction = []
for _ in range(L):
    direction.append(list(input().split()))


