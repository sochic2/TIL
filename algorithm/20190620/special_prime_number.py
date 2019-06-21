import sys, math
sys.stdin = open("special_primenumber.txt")


prime_arr = [0, 0] + [1] * (10 **6)
for i in range(2, 10**3):
    if prime_arr[i] == 1:
        j = 2
        while i*j <= 10**6:
            prime_arr[i*j] = 0
            j += 1 
# print(prime_arr[13])
def find(num):
    global D
    for i in str(num):
        if str(D) == i:
            
            return True
   
    return False

T = int(input())

for tc in range(1, T+1):
    D, A, B = map(int, input().split())

    result = 0
    for i in range(A, B+1):
        if prime_arr[i]:
            if find(i):
                result += 1

    print("#{} {}".format(tc, result))
