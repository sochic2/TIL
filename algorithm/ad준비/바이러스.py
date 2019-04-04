def dfs(no):
    for i in range(1, computer+1):
        if arr[no][i] == 1 and result[no] == 1 and result[i] != 1:
            result[i] = 1
            dfs(i)

computer = int(input())
link = int(input())
data = [list(map(int, input().split())) for _ in range(link)]

# print(data)
arr = [[0] * (computer+1) for _ in  range(computer+1)]
# print(arr)
for i in range(link):
    arr[data[i][0]][data[i][1]] = 1
    arr[data[i][1]][data[i][0]] = 1

result = [0] * (computer +1)
result[1] = 1

dfs(1)
# print(result)
print(sum(result)-1)
