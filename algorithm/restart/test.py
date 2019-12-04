def fake(n):
    dfs(n)


def dfs(n):
    if n == 495:
        print(2000)
        return
    else:
        fake(n+1)


dfs(0)