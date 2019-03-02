import sys
sys.stdin = open('마을위성사진.txt')

arr = []
N = int(input())
for _ in range(N):
    arr += [list(map(int, input()))]
# print(town)
solution = 0

for h in range(N):
    flag = 0
    for i in range(1, N-1):
        for j in range(1, N-1):
           if arr[i][j] > h:
               flag = 1
               if arr[i-1][j] > h and arr[i+1][j] > h and arr[i][j+1] > h and arr[i][j-1] > h:
                    arr[i][j] += 1
    if flag == 0 :

        break
print(h)

# for i in range(1, N):
#     for j in range(1, N):
#         if arr[i][j] > solution:
#             solution = arr[i][j]



# print(solution)