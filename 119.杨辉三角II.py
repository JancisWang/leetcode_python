'''
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        i = 2
        prev = [1, 1]
        while i <= rowIndex:
            prev = [1] + [a + b for a, b in zip(prev[:-1], prev[1:])] + [1]
            i += 1
        return prev


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r = [1]
        for i in range(1, rowIndex + 1):
            r.insert(0, 0)
            for j in range(i):
                r[j] += r[j+1]
        return r