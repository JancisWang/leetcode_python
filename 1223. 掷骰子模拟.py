'''
有一个骰子模拟器会每次投掷的时候生成一个 1 到 6 的随机数。

不过我们在使用它时有个约束，就是使得投掷骰子时，连续 掷出数字 i 的次数不能超过 rollMax[i]（i 从 1 开始编号）。

现在，给你一个整数数组 rollMax 和一个整数 n，请你来计算掷 n 次骰子可得到的不同点数序列的数量。

假如两个序列中至少存在一个元素不同，就认为这两个序列是不同的。由于答案可能很大，所以请返回 模 10^9 + 7 之后的结果。

 

示例 1：

输入：n = 2, rollMax = [1,1,2,2,2,3]
输出：34
解释：我们掷 2 次骰子，如果没有约束的话，共有 6 * 6 = 36 种可能的组合。但是根据 rollMax 数组，数字 1 和 2 最多连续出现一次，所以不会出现序列 (1,1) 和 (2,2)。因此，最终答案是 36-2 = 34。
示例 2：

输入：n = 2, rollMax = [1,1,1,1,1,1]
输出：30
示例 3：

输入：n = 3, rollMax = [1,1,1,2,2,3]
输出：181
 

提示：

1 <= n <= 5000
rollMax.length == 6
1 <= rollMax[i] <= 15

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dice-roll-simulation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[[0 for i in range(16)] for _ in range(7)] for j in range(n+1)]
        mod = 10**9 + 7

        for i in range(1, n+1):
            for j in range(1, 7):
                if i==1:
                    dp[i][j][1] = 1
                    continue
                
                for k in range(2, rollMax[j-1]+1):
                    dp[i][j][k] = dp[i-1][j][k-1]

                res = 0
                for l in range(1, 7):
                    if l != j:
                        for kk in range(1, 16):
                            res += dp[i-1][l][kk]
                            res %= mod
                dp[i][j][1] = res
        s = 0
        for j in range(1, 7):
            for k in range(1, 16):
                s += dp[n][j][k]
                s %= mod
        return s







