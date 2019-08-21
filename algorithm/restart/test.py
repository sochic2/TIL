def dfs(n):
    global N
    if n >= 3:
        print(arr)
    else:

        arr[n] = 1
        dfs(n+1)
        arr[n] = 0
        dfs(n+1)



N = 3
arr = [0, 0, 0]
dfs(0)
