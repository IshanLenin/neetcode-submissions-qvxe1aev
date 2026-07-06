class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [float("inf")] * (COLS + 1)
        dp[COLS - 1] = 0

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                dp[c] = grid[r][c] + min(dp[c], dp[c + 1])

        return dp[0]