import sys
sys.stdin = open('회전_input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    print(f'#{tc} {data[M%N]}')