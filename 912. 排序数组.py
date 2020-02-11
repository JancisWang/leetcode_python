'''

给定一个整数数组 nums，将该数组升序排列。

 

示例 1：

输入：[5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：[5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
 

提示：

1 <= A.length <= 10000
-50000 <= A[i] <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quicksort(nums, 0, len(nums)-1)
        
    def quicksort(self, nums, start, end):
        left = start
        right = end
        if left > right:
            return 
        mid = nums[start]
        while left < right:
            while left < right and nums[right] >= mid:
                right -= 1
            nums[left]= nums[right]
            while left < right and nums[left] < mid:
                left += 1
            nums[right] = nums[left]
        nums[left] = mid
        self.quicksort(nums, start, left-1)
        self.quicksort(nums, left+1, end)
        return nums
