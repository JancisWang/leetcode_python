
'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
在真实的面试中遇到过这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0: return []
        triangle = []
        triangle.append([1])
        for i in range(1, numRows):
            temp = [1 for _ in range(i+1)]
            for j in range(1, i):
                temp[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(temp)
        return triangle
            


