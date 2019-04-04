import sys
sys.stdin = open('최소신장트리.txt')
T = int(input())

def find_set(w):
    if visit[w] == w:
        return w
    else:
        return find_set(visit[w])

def mst():
    global ssum

    for i in range(len(data)):
        p1 = find_set(data[i][0])
        p2 = find_set(data[i][1])
        if p1 != p2:
            ssum += data[i][2]
            visit[p2] = p1


# 강사님 while 이용
# def mst_teacher():
#     global ssum
#     c = 0
#     s = 0
#     i = 0
#
#     while c < V:
#         p1 = find_set(data[i][0])
#         p2 = find_set(data[i][1])
#         if p1 != p2:
#             s += data[i][2]
#             c += 1
#             visit[p2] = p1
#         i += 1
#     return s


for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]
    data.sort(key=lambda x: x[2])

    visit = list(range(V+1))   # make_set
    ssum = 0
    mst()
    # print('#{} {}'.format(tc, mst_teacher()))
    print(visit)
    print('#{} {}'.format(tc, ssum))
    
