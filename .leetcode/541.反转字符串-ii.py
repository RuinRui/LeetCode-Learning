#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

from typing import List
# @lc code=start


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        start, step = 0, 2 * k
        result = list(s)
        length = len(result)
        while start < length:
            end = start + k - 1
            left, right = start, end if end < length else length - 1
            while left < right:
                result[left], result[right] = result[right], result[left]
                left += 1
                right -= 1

            start += step

        return ''.join(result)


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    result = s.reverseStr("abcdefgh", 3)
    print(result)
