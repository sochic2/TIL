import sys
sys.stdin = open('배열최소합_input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(data)