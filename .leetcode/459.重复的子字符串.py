#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        news = s[1:] + s[:-1]
        next = self.getNextArr(s)
        j = 0
        for c in news:
            while j > 0 and s[j] != c:
                j = next[j - 1]

            if s[j] == c:
                j += 1

            if j >= len(next):
                return True

        return False

    def getNextArr(self, s: str) -> list:
        j, next = 0, [0 for i in s]
        for i in range(1, len(s)):
            while j > 0 and s[j] != s[i]:
                j = next[j - 1]

            if s[i] == s[j]:
                j += 1

            next[i] = j

        return next


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    result = s.repeatedSubstringPattern("a")
    print(result)
