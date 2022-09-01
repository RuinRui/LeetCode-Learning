#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

from typing import List
# @lc code=start


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    result = s.reverseString(["h", "e", "l", "l", "o"])
    print(result)
    result = s.reverseString(["H", "a", "n", "n", "a", "h"])
    print(result)

    result = s.reverseString(["H"])
    print(result)
