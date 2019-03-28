
def hard(N, s, ssum):
    global hard_sum
    if N == s :
        if ssum < hard_sum:
            hard_sum = ssum

    else:
        for i in parr:
            hard_arr[s] = i
            ssum_mid = ssum + arr[s][i]
            if ssum_mid < hard_sum:
                hard(N, s+1, ssum_mid)

def perm(N, s, ssum):
    global perm_sum
    if N == s:
        if ssum < perm_sum:
            perm_sum = ssum
    else:
        for i in range(s, N):
            parr[i], parr[s] = parr[s], parr[i]
            mid_ssum = ssum + arr[s][parr[s]]
            if mid_ssum < perm_sum:
                perm(N, s+1, mid_ssum)
            parr[i], parr[s] = parr[s], parr[i]



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
perm_sum = 987654321

hard_sum = 987654321

parr = list(range(N))
hard_arr = [0] * N
perm(N, 0, 0)
hard(N, 0, 0)

print(hard_sum)
print(perm_sum)