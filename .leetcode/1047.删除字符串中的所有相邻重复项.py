#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start


class Solution:
    def removeDuplicates(self, s: str) -> str:
        l = []
        for c in s:
            if l and l[-1] == c:
                l.pop()
            else:
                l.append(c)

        return "".join(l)


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    result = s.removeDuplicates("aabxbbxcac")
    print(result)
