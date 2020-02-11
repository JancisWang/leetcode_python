'''

在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。

返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望索引的数字  i < j 且有 (time[i] + time[j]) % 60 == 0。

 

示例 1：

输入：[30,20,150,100,40]
输出：3
解释：这三对的总持续时间可被 60 整数：
(time[0] = 30, time[2] = 150): 总持续时间 180
(time[1] = 20, time[3] = 100): 总持续时间 120
(time[1] = 20, time[4] = 40): 总持续时间 60
示例 2：

输入：[60,60,60]
输出：3
解释：所有三对的总持续时间都是 120，可以被 60 整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pairs-of-songs-with-total-durations-divisible-by-60
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        d = collections.defaultdict(int)
        for num in time:
            d[num % 60] += 1
        for i in range(1, 30):
            count += d[i] * d[60 - i]
        count += d[0] * (d[0]-1) // 2
        count += d[30] * (d[30]-1)//2
        
        return count


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        time = [t % 60 for t in time]
        d = collections.defaultdict(int)
        for t in time:
            residual = (60 -t) % 60
            count += d[residual]
            d[t] += 1
        return count

