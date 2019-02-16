import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(T):
    N, K = map(int,input().split())
    data = list(input())
    # print(T)
    # print(N, K)
    # print(data)
    one_rectangle = N//4
    # print(one_rectangle)
    numbers = []
    final_numbers = []

    for _ in range(one_rectangle):
        data.insert(0, data.pop())
        for i in range(4):
            numbers += [data[i * one_rectangle:one_rectangle+i*one_rectangle]]


    final_data = []
    for j in numbers:
        if j not in final_data:
            final_data += [''.join(j)]
    # print(final_data)

    for k in final_data:
        if int(k, 16) not in final_numbers:
            final_numbers.append(int(k, 16))
    final_numbers.sort()
    # print(final_numbers)
    print(f'#{tc+1} {final_numbers[-K]}')