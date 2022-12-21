class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mapp = [[0]*m for _ in range(n)]
        for x in range(m):
            mapp[0][x] = 1

        for y in range(n):
            mapp[y][0] = 1

        for y in range(n):
            for x in range(m):
                if mapp[y][x] == 0:
                    mapp[y][x] = mapp[y-1][x] + mapp[y][x-1]
        for r in mapp:
            print(r)
        return mapp[n-1][m-1]


ins_so = Solution().uniquePaths(2,3)
