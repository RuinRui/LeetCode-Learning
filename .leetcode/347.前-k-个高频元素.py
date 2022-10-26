#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

import heapq
from typing import List
# @lc code=start


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nmap = {}
        for i in range(len(nums)):
            nmap[nums[i]] = nmap.get(nums[i], 0) + 1

        priQue = []
        for key, v in nmap.items():
            # 每次移动的时间复杂度是logK，一共2logK
            heapq.heappush(priQue, (v, key))
            if len(priQue) > k:
                heapq.heappop(priQue)

        result = [0] * k
        for i in range(k-1, -1, -1):  # 倒序输出堆里的数据，因为是小顶堆
            result[i] = heapq.heappop(priQue)[1]

        return result
# 堆排序


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    result = s.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    print(result)
    result = s.topKFrequent([1, 4, 4, 6, 6, 2], 2)
    print(result)
