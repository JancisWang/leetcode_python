'''
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


# 动态规划 （可以分解为独立子问题， 并且存在重复（因为只是计数，和具体树节点的数字无关））
class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n+1)
        G[0] = 1
        G[1] = 1
        for i in range(2, n+1):
            for j in range(i+1):
                G[i] += G[j-1] * G[i-j]
        return G[n]


# 超出时间限制
class Solution:
    def numTrees(self, n: int) -> int:
        def count_tree(b, e):
            if b>e:return 1
            count_all = 0
            for i in range(b, e+1):
                left_tree = count_tree(b, i-1)
                right_tree = count_tree(i+1, e)
                count_all = left_tree*right_tree + count_all
            return count_all
        return count_tree(1, n) if n else 0