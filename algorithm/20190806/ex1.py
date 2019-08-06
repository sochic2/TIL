import sys
import copy
sys.stdin = open("ex1_input.txt")

def gorot():
    while rotation:
        ind = rotation.pop(0)
        realrot(ind)
    return

def realrot(arr):
    flag = [0, 0, 0, 0, 0]
    for i in range(4):
        if rotation[i] != rotation[i+1]:
            flag[i] = 1

    flag

    return

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    mag = [list(map(int, input().split())) for _ in range(4) ]
    rotation = [list(map(int, input().split())) for _ in range(K)]
    gorot()