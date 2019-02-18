import sys
sys.stdin = open('workshop_input.txt')

T = 10
for tc in range(T):
    V, E = map(int, input().split())

    works = [i for i in range(1, V+1)]
    start = []
    end = []
    queue = []
    queue_2 = []
    data = list(map(int, input().split()))

    start = data[0::2]
    end = data[1::2]



    while sum(start) != 0:
        for idx, value in enumerate(start):
            if value != 0 and value not in end:
                queue.append(start[idx])
                end[idx] = 0
                start[idx] = 0

    for o in queue:
        if o not in queue_2:
            queue_2.append(o)

    for k in works:
        if k not in queue_2:
            queue_2.append(k)


    result = ' '.join(map(str, queue_2))
    print(f'#{tc + 1} {result}')
