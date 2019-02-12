import sys
sys.stdin = open("종이붙히기_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    N = int(N/10)
    # print('T는:', T)
    # print(f'{tc+1}')
    # print(N)

    def func(N):
        if N == 1:
            return 1
        return (2**N) - func(N-1)

    print(f'#{tc+1} {func(N)}')