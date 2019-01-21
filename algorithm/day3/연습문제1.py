arr = [[1, 1, 1, 1, 1],
       [1, 0, 0, 0, 1],
       [1, 0, 0, 0, 1],
       [1, 0, 0, 0, 1],
       [1, 1, 1, 1, 1]]
def isWall(x, y):
    if x<0 or x>=5: return True
    if y<0 or y>=5: return True
    return False
def calAbs(y, x):
    if y-x > 0 : return y-x
    else: return x-y


#나중에받아올때...?
# arr = [[0 for _ in range(5)] for _ in range(5)]
#                 #열,                 행
# print(arr)
#
# for i in range(5):
#     arr[i] = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ssum = 0

for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if isWall(testX, testY) == False:
                ssum += calAbs(arr[y][x], arr[testY][testX])

print(ssum)

