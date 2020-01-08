key = [[0, 0], [0, 1]]
lock = [[0, 1, 1], [1, 1, 1], [1, 1, 1]]


def turn(key):
    temp = [[0] * len(key) for _ in range(len(key))]
    for y in range(len(key)):
        for x in range(len(key)):
            temp[y][x] = key[x][len(key)-1-y]
    return temp

def multi(key, lock, N, M):

    biglock = [[0] * (N + (M-1)*2) for _ in range(N + (M-1)*2)]
    for y in range(N):
        for x in range(N):
            biglock[y+M-1][x+M-1] = lock[y][x]

    return biglock

def check(N, M, biglock):
    for y in range(N):
        for x in range(N):
            if biglock[y+M-1][x+M-1] != 1:
                return False
    return True

def solution(key, lock):
    answer = False
    N = len(lock)
    M = len(key)
    keys = [key]

    # key 돌린거 추가하기
    for i in range(3):
        keys.append(turn(keys[i]))

    for i in range(4):
        for y in range(M+N-1):
            for x in range(M+N-1):
                biglock =  multi(key, lock, N, M)
                for r in range(M):
                    for c in range(M):
                        biglock[y+r][x+c] += keys[i][r][c]
                if check(N, M, biglock) == True:
                    return True

    return False




print(solution(key, lock))