#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = [0 for i in range(27)]
        for c in magazine:
            counter[ord(c) - 97] += 1

        for c in ransomNote:
            counter[ord(c) - 97] -= 1
            if counter[ord(c) - 97] < 0:
                return False

        return True


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    result = s.canConstruct("aa", "ab")
    print(result)
