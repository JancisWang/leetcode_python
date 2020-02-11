'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        sum_m = 0
        for num in nums:
            if sum_m > 0:
                sum_m += num
            else:
                sum_m = num
            ans = max(sum_m, ans)
        return ans

# 动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        maxsum = nums[0]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            if maxsum < dp[i]:
                maxsum = dp[i]
        return maxsum

# 分治法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        mid = len(nums)//2
        maxleft = self.maxSubArray(nums[:mid])
        maxright = self.maxSubArray(nums[mid:])
        sum_l = 0
        max_l = nums[mid-1]
        for i in range(mid-1, -1, -1):
            sum_l += nums[i]
            max_l = max(max_l, sum_l)
        sum_r = 0
        max_r = nums[mid]
        for i in range(mid, len(nums)):
            sum_r += nums[i]
            max_r = max(max_r, sum_r)
        return max(maxleft, maxright, max_l + max_r)

