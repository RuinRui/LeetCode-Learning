#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        m = dict()
        for c in s:
            if c not in m.keys():
                m[c] = 0
            m[c] += 1

        for c in t:
            if c not in m.keys():
                return False
            m[c] -= 1

        for k, v in m.items():
            if v != 0:
                return False

        return True


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    result = s.isAnagram("rat", "car")
    print(result)
