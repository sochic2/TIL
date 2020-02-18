r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
marr = [[0]*100 for _ in range(100)]
for y in range(3):
    for x in range(3):
        marr[y][x] = arr[y][x]

R = 3
C = 3
result = -1
t = 0
while t < 101:
    if marr[r-1][c-1] == k:
        result = t
        break
    if R >= C:

        for y in range(R):
            ttu = []
            for x in range(C):
                if marr[y][x] == 0:continue
                flag = 0
                for o in range(len(ttu)):
                    if ttu[o][1] == marr[y][x]:
                        ttu[o][0] += 1
                        flag = 1
                if flag == 0:
                    ttu.append([1, marr[y][x]])
                marr[y][x] = 0

            ttu.sort()
            C = max(C, len(ttu) * 2)
            z = 0
            for count, num in ttu:
                if z == 100:break
                marr[y][z], marr[y][z+1] = num, count
                z += 2


    else:

        for x in range(C):
            ttu = []
            for y in range(R):
                if marr[y][x] == 0:continue
                flag = 0
                for o in range(len(ttu)):
                    if ttu[o][1] == marr[y][x]:
                        ttu[o][0] += 1
                        flag = 1
                if flag == 0:
                    ttu.append([1, marr[y][x]])
                marr[y][x] = 0
            ttu.sort()
            R = max(R, len(ttu) * 2)
            z = 0
            for count, num in ttu:
                if z == 100:break
                marr[z][x], marr[z+1][x] = num, count
                z += 2

    t += 1
print(result)