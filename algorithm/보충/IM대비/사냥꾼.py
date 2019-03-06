import sys
sys.stdin = open('사냥꾼.txt')
N = int(input())
data = []
for _ in range(N):
    data += [list(map(int, input()))]

y_wall = [0] * (N+2)

for i in data:
    i.append(0)
    i.insert(0, 0)

data.append(y_wall)
data.insert(0, y_wall)



cnt = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        if data[i][j] == 1:

            if data[i+1][j] == 2 or data[i+1][j] == 9:
                k = 1

                while True:
                    if data[i+k][j] == 2 or data[i+k][j] == 9:
                        data[i + k][j] = 9
                        cnt += 1
                        k+=1
                    elif data[i+k][j] == 1 or data[i+k][j] == 0:
                        break
                    else:
                        k+=1

            if data[i-1][j] == 2 or data[i-1][j] == 9:
                k = 1

                while True:
                    if data[i-k][j] == 2 or data[i-k][j] == 9:
                        data[i - k][j] = 9
                        cnt += 1
                        k+=1
                    elif data[i-k][j] == 1 or data[i-k][j] == 0:
                        break
                    else:
                        k+=1

            if data[i][j+1] == 2 or data[i][j+1] == 9:
                k = 1

                while True:
                    if data[i][j+k] == 2 or data[i][j+k] == 9:
                        data[i][j + k] = 9
                        cnt += 1
                        k+=1
                    elif data[i][j+k] == 1 or data[i][j+k] == 0:
                        break
                    else:
                        k+=1

            if data[i][j-1] == 2 or data[i][j-1] == 9:
                k = 1

                while True:
                    if data[i][j-k] == 2 or data[i][j-k] == 9:
                        data[i][j - k] = 9
                        cnt += 1
                        k+=1
                    elif data[i][j-k] == 1 or data[i][j-k] == 0:
                        break
                    else:
                        k+=1

            if data[i+1][j+1] == 2 or data[i+1][j+1] == 9:
                k = 1

                while True:
                    if data[i+k][j+k] == 2 or data[i+k][j+k] == 9:
                        data[i + k][j + k] =9
                        cnt += 1
                        k+=1
                    elif data[i+k][j+k] == 1 or data[i+k][j+k] == 0:
                        break
                    else:
                        k+=1

            if data[i-1][j-1] == 2 or data[i-1][j-1] == 9:
                k = 1

                while True:
                    if data[i-k][j-k] == 2 or data[i-k][j-k] == 9:
                        data[i - k][j - k] =9
                        cnt += 1
                        k+=1
                    elif data[i-k][j-k] == 1 or data[i-k][j-k] == 0:
                        break
                    else:
                        k+=1

            if data[i+1][j-1] == 2 or data[i+1][j-1] == 9:
                k = 1

                while True:
                    if data[i+k][j-k] == 2 or data[i+k][j-k] == 9:
                        data[i + k][j - k] = 9
                        cnt += 1
                        k+=1
                    elif data[i+k][j-k] == 1 or data[i+k][j-k] == 0:
                        break
                    else:
                        k+=1

            if data[i-1][j+1] == 2 or data[i-1][j+1] == 9:
                k = 1

                while True:

                    if data[i-k][j+k] == 2 or data[i-k][j+k] == 9:
                        data[i - k][j + k] = 9
                        cnt += 1
                        k+=1
                    elif data[i-k][j+k] == 1 or data[i-k][j+k] == 0:
                        break
                    else:
                        k+=1

# print(cnt)
result = 0
for i in data:
    result += i.count(9)

# for i in data:
#     print(*i)

print(result)
