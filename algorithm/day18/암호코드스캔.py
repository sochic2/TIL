import sys
sys.stdin = open('암호코드스캔.txt')

binary_num = [[0,0,0,0], #0
              [0,0,0,1], #1
              [0,0,1,0], #2
              [0,0,1,1], #3
              [0,1,0,0], #4
              [0,1,0,1], #5
              [0,1,1,0], #6
              [0,1,1,1], #7
              [1,0,0,0], #8
              [1,0,0,1], #9
              [1,0,1,0], #A
              [1,0,1,1], #B
              [1,1,0,0], #C
              [1,1,0,1], #D
              [1,1,1,0], #E
              [1,1,1,1], #F
]

psw = [[2, 1, 1],
       [2, 2, 1],
       [1, 2, 2],
       [4, 1, 1],
       [1, 3, 2],
       [2, 3, 1],
       [1, 1, 4],
       [3, 1, 2],
       [2, 1, 3],
       [1, 1, 2]
       ]

o_T = ['A', 'B', 'C', 'D', 'E', 'F']
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    change_data = [[] for _ in range(N)]


    for i in range(N):
        for j in range(M):
            if data[i][j] in o_T:
                change_data[i] += binary_num[ord(data[i][j]) - ord('A') + 10]
            else:
                change_data[i] += binary_num[int(data[i][j])]

    result = []
    flag = 0
    for i in range(len(change_data)):
        if sum(change_data[i]):
            for j in range(len(change_data[i]), -1, -1):
                if change_data[i][j] == 1 and change_data[i-1][j] == 0:



