#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1) + 1
        cols = len(text2) + 1

        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        for row in range(rows-2,-1,-1):
            for col in range(cols-2,-1,-1):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row+1][col], dp[row][col+1])
        return dp[0][0]

        
        
# @lc code=end

