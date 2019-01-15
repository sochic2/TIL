import sys
sys.stdin = open("Flatten_input.txt")

for n in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))

    boxes_num = boxes[0]

    for i in range(N):
        for i in range(len(boxes)):
            if boxes_num < boxes[i]:
                boxes_num = boxes[i]
                boxes_number = i
        boxes[boxes_number] += -1

        for i in range(len(boxes)):
            if boxes_num > boxes[i]:
                boxes_num = boxes[i]
                boxes_number = i
        boxes[boxes_number] += 1
    for i in range(len(boxes) - 1, 0, -1):
        for j in range(i):
            if boxes[j] < boxes[j + 1]:
                boxes[j], boxes[j + 1] = boxes[j + 1], boxes[j]
    max_num = boxes[0]
    min_num = boxes[-1]
    result = max_num - min_num
    print(f'#{n} {result}')