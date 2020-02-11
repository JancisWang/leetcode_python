'''
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。

 

示例：

输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
 

提示：

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-array-by-parity-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i = 0
        if len(A) % 2 == 0:
            j = len(A) - 1
        else:
            j = len(A) - 2
        while i < len(A) and j > 0:
            if A[i] % 2 != 0 and A[j] % 2 == 0:
                odd = A[i]
                A[i] = A[j]
                A[j] = odd
                i += 2 
                j -= 2
            elif A[i] % 2 == 0:
                i += 2
            else:
                j -= 2
        return A


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(A)-1, 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A

            
