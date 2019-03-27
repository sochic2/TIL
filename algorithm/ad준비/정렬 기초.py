#버블 정렬 이용    O(n**2)
# 첫번쨰 루프 : 정렬 대상, 회전 수 제어
# 두번째 루프 : 비교 대상

#기본 구조
a = [5, 3, 1, 4, 2]  #총점
b = [4, 2, 1, 3, 1]  #국어점수
N = len(a)
for i in range(N-1):   # N-1  부분을 조작해서 N개중 M개만 sorting 가능 ex) 3등까지만 뽑기 이런때 쓸듯?
    for j in range(i+1, N):
        if (a[i] > a[j]):       # 교환 조건
            a[i], a[j] = a[j], a[i]

        if a[i] == a[j] and b[i] < b[j]:   # 2번쨰 조건, ex) 총점 같을시 국어점수 높은사람을 앞으로
            bye

# quick sort
# pivot : 기준
# left : 비교대상
# Target: 교환대상
# 비교 : P <=> L
# 교환 : L <=> T


                      # pivot    그 왼쪽 모든 것이 비교 대상 left 라고 이름붙이심 그냥
                      # L이  왼쪽에서 오른쪽으로 한칸씩 이동하면서 pvito 과 비교해서 보다 크면 두고 보다 작으면 target과 교환, 교환 되면 target도 한칸 오른쪽으로 이동
                      # 한회전이 끝나면 pivot과 Target 마지막 위치의 값을 교환.  왜냐면 1회전 하면 마지막 타겟 위치 왼편에 초기 pivot값보다 작은애들 우측에 보다 큰애들이
                      # 위치함.
          # 0    #N-1
def Qsort(start, end):
    if start >= end: return
    P, T = end, start
    for L in range(start, end):
        if quick[L]  < quick[P]:
            quick[L], quick[T] = quick[T], quick[L]
            T += 1
    quick[P], quick[T] = quick[T], quick[P]
    Qsort(start, T-1)
    Qsort(T+1, end)
quick = [1, 6, 3, 4, 5]

s = 0
e = len(quick)-1
Qsort(s, e)
print(quick)

# merge sort    O(N*logN)
#  8 => 4 & 4 => 2 & 2 & 2 & 2 => 1 1 1 1 1 1 ...
# 뎁스는 log N    루프는 N
# 토너먼트 카드게임하고 비슷해
# 일단 1개가 될때까지 쭉 내려가서 일하면서 올라오기



def Msort(s, e):
    if s>=e: return

    m = (s+e)//2
    Msort(s, m)
    Msort(m+1, e)
    L, R, T = s, m+1, s

    while L <= m and R<=e:
        if arr[L] < arr[R]:
            Temp[T] = arr[L]
            T += 1
            L += 1
        else:
            Temp[T] = arr[R]
            T += 1
            R += 1

    while L <= m:
        Temp[T] = arr[L]
        T += 1
        L += 1

    while R <= e:
        Temp[T] = arr[R]
        T += 1
        R += 1

    for i in range(s, e+1):
        arr[i] = Temp[i]


arr = [5, 3, 1, 6, 2, 4]
Temp = [0] * 6
Msort(0, 5)
print(arr)



