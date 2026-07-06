class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M,N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * (N+1)
        dp[N-1] = 1

        for r in reversed(range(M)):
            for c in reversed(range(N)):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                else:
                    dp[c] += dp[c+1]
        return dp[0]