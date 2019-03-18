data = '0269FAC9A0'
o_T = ['A', 'B', 'C', 'D', 'E', 'F']

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

psw= [[0, 0, 1, 1, 0, 1],
      [0, 1, 0, 0, 1, 1],
      [1, 1, 1, 0, 1, 1],
      [1, 1, 0, 0, 0, 1],
      [1, 0, 0, 0, 1, 1],
      [1, 1, 0, 1, 1, 1],
      [0, 0, 1, 0, 1, 1],
      [1, 1, 1, 1, 0, 1],
      [0, 1, 1, 0, 0, 1],
      [1, 0, 1, 1, 1, 1],
      ]

binary_num = []
for i in range(len(data)):
    if data[i] in o_T:
        for j in range(4):
            binary_num.append(int(a[ord(data[i]) - ord('A')+10][j]))
    else:
        for j in range(4):
            binary_num.append(int(a[i][j]))
print(binary_num)

flag = 0
for i in range(len(binary_num)):

    if binary_num[i:i+6] in psw:
        flag = 1

        while i+6 <= len(binary_num):
            for j in range(len(psw)):
                if psw[j] == binary_num[i:i+6]:
                    print(j, end=' ')
                    i += 6
    if flag == 1: break


