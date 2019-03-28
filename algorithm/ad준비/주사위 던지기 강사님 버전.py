def DFS(no):
    if no > N:
        for i in range(1, N+1):
            print(rec[i], end=' ')
        print()
        return
    for i in range(1, 7):
        rec[no] = i
        DFS(no + 1)

#
# def DFS2(no):
#     if no > N:
#         for i in range(1, N+1): print(rec[i], end=' ')
#         print()
#         return
#     for i in range(1, 7):
#         if chk[i] : continue
#         chk[i] = 1
#         rec[no] = 1
#         DFS2(no +1)
#         chk[i] = 0

# def DFS3(no, nsum):
#     if no>N :
#         if nsum == M:
#             for i in range(1, N+1): print(rec[i], end= ' ')
#             print()
#         return
#     for i in range(1, 7):
#         rec[no] = i
#         DFS3(no+1, nsum + i)


N, M = map(int, input().split())
rec = [0] * 8
chk = [0] * 7
DFS(1)
# DFS2(1)
# DFS3(1, 0)