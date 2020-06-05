# combination
# def dfs(n, k):
#     if n == 3:
#         print(result)
#         return
#
#     for i in range(k, N):
#         result[n] = i
#         dfs(n+1, i+1)
#         result[n] = 0
#
#
# N = 5
# check = [0] * N
# result = [0, 0, 0]
# dfs(0, 0)


# 5*4*3/3*2*1

#permutation
#
def dfs(n):
    global solution
    if n == N:
        solution += 1
        print(result)
        return
    for i in range(N):
        # if check[i] == 1:continue
        result[n] = i
        # check[i] = 1
        dfs(n+1)
        # check[i] = 0
        result[n] = 0

solution = 0
N = 3
check = [0] * N
result = [0] * N
dfs(0)
print(solution)


# a = [1,2,3, 4, 5, 6, 7, 8, 9, 10] # 구슬
# b = [0] * 10 # 구슬을 담을 상자
# chk = [0] * 10 # 구슬 사용여부 체크
# N = 10
#
# def DFS(no): #현재 no번째 상자에 모든 구슬을 순열구조로 담아보는 모든 경우
#     #1] 리턴조건 : 3개를 고른후 인쇄한 후 리턴
#     if no == N:
#         print(*b)
#         return
#     #2] a배열에서 0요소부터 N전요소전까지 고르는 모든 경우(단 구슬중복 배제)
#     else:
#         for i in range(N):      # a배열의 구슬(단 중복 배제)
#             if chk[i]: continue
#             else:
#                 chk[i] = 1              #체크 존재 유무로 중복순열이냐 아니냐이냐 아니냐
#                 b[no] = a[i]
#                 DFS(no + 1)
#                 chk[i] = 0



# main ============================
# DFS(0) # b[0]요소부터 담기 시작