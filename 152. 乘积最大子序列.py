'''
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 动态规划， 维护一个imax 和 imin， 如果是负数， 对换两个的值

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:return 0
        if len(nums)==1:return nums[0]

        imax = 1
        imin = 1
        ans = float('-inf')
        for num in nums:
            if num < 0:
                temp = imax
                imax = imin
                imin = temp
            imax = max(imax * num, num)
            imin = min(imin * num, num)
            ans = max(ans, imax)
        return ans


# 理解简化题目：
# 1）如果给定数组都是正数，全部相乘即最大
# 2）如果存在偶数个负数，也是全部相乘
# 3）如果奇数个负数，要么舍弃最后一个负数及之后的树 ， 要么舍弃第一个负数及之前的数
# 对于0的处理， 理解为几个独立的数组， 每次遇到0 max重置即可
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:return 0
        if len(nums)==1:return nums[0]

        imax = 1
        res = nums[0]
        for num in nums:
            imax *= num
            res = max(res, imax)
            if num==0:
                imax = 1
        imax = 1
        for num in nums[::-1]:
            imax *= num
            res = max(res, imax)
            if num == 0:
                imax = 1
                
        return res




