#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   HASH_454.py
@Time    :   2021/09/16 20:44:40
@Author  :   Abel

给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。
例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List
import collections


class Solution:
    # 超简短代码，摘自评论区，但是建议大家不熟悉库函数原理的情况下别用，当个乐呵，熟悉的话请
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dic = collections.Counter(a + b for a in A for b in B)
        return sum(dic.get(- c - d, 0) for c in C for d in D)

    def fourSumCount_1(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dic, counts = {}, 0
        for n1 in nums1:
            for n2 in nums2:
                sum = n1 + n2
                if sum in dic.keys():
                    dic[sum] += 1
                else:
                    dic[sum] = 1

        keys = dic.keys()
        for n3 in nums3:
            for n4 in nums4:
                sum = -(n3 + n4)
                if sum in keys:
                    count = dic[sum]
                    counts += count

        return counts


if __name__ == '__main__':
    s = Solution()
    result = s.fourSumCount([-1, -1],
                            [-1, 1],
                            [-1, 1],
                            [1, -1])
    print(result)
