import sys
sys.stdin = open("num_card_sample_input.txt")
T = int(input())
for test_case in range(1, T+1):
    C = [0] * 10
    N = int(input())
    data = input()

    for i in range(N):
        C[int(data[i])] += 1

    maxIndex = 0