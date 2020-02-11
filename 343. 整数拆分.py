'''
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 动态规划
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(dp[j],j)* max(dp[i-j], i-j))
        return dp[-1]


# 贪心算法
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n-1
        a = n // 3
        b = n % 3
        if b == 0: return 3**a
        if b == 1: return 3**(a-1) * 4
        if b == 2: return 3**a * 2
