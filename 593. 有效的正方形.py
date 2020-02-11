'''
给定二维空间中四点的坐标，返回四点是否可以构造一个正方形。

一个点的坐标（x，y）由一个有两个整数的整数数组表示。

示例:

输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
输出: True
 

注意:

所有输入整数都在 [-10000，10000] 范围内。
一个有效的正方形有四个等长的正长和四个等角（90度角）。
输入点没有顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        ls = [p1, p2, p3, p4]
        ls.sort(key=lambda x:(x[0], x[1]))
        def dist(x, y):
            return (x[0]-y[0])**2 + (x[1]-y[1])**2
        
        return dist(ls[0], ls[1]) == dist(ls[0], ls[2]) == dist(ls[1], ls[3]) == dist(ls[2], ls[3])!= 0 and dist(ls[0], ls[3])==dist(ls[1], ls[2])