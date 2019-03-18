import sys
sys.stdin = open('연습문제2.txt')
data = list(map(str, input()))
print(data)

a = [[0, 0, 0, 0],  #0
     [0, 0, 0, 1],  #1
     [0, 0, 1, 0],  #2
     [0, 0, 1, 1],  #3
     [0, 1, 0, 0],  #4
     [0, 1, 0, 1],  #5
     [0, 1, 1, 0],  #6
     [0, 1, 1, 1],  #7
     [1, 0, 0, 0],  #8
     [1, 0, 0, 1],  #9
     [1, 0, 1, 0],  #A
     [1, 0, 1, 1],  #B
     [1, 1, 0, 0],  #C
     [1, 1, 0, 1],  #D
     [1, 1, 1, 0],  #E
     [1, 1, 1, 1],  #F
     ]
result = []
o_T = ['A', 'B', 'C', 'D', 'E', 'F']
solution = []
for i in data:
    if i in o_T:
        for j in range(4):
            result.append(a[10+ord(i)-ord('A')][j])
    else:
        for j in range(4):
            result.append(a[int(i)][j])
print(result)


solution = []
ssum = 0
for i in range(len(result)):
    solution += [result[i]]
    if len(solution) == 7:
        for j in range(7):
            # print(result)
            ssum += solution[j] * 2**(6-j)

        print(ssum, end=" ")
        solution = []
        ssum = 0


if i % 7 != 6:
    for j in range(len(solution)):
        ssum += solution[j] * 2 **(len(solution)-j-1)
    
    print(ssum)
