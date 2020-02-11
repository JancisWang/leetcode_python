'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        nums.sort()
        if nums[0] * nums[-1] > 0: return []
        n = len(nums)
        res = []
        i = 0
        while i < n - 2:
            if nums[i] * nums[-1] <= 0:
                left = i + 1
                right = n - 1
                while left < right:
                    result = nums[i] + nums[left] + nums[right]
                    if result > 0:
                        right -= 1
                        while left < right and nums[right]==nums[right+1]:
                            right -=1
                    elif result < 0:
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                    else:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left -1]:
                            left += 1
                        while left < right and nums[right] == nums[right +1]:
                            right -= 1
            i += 1
            while i < n-2 and nums[i]==nums[i-1]:
                i += 1
        return res
