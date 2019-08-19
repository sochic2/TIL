import sys
sys.stdin = open('3260')
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    print('#{} {}'.format(tc, sum(arr)))