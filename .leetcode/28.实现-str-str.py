#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
# KMP算法，KMP算法的目的是在一个字符串中找出一个子串，比如下面的在A字符串中找B字符串
# A: aabaabaafa
# B: aabaaf
# KMP的核心就是前缀表，前缀表是用来回退的，它记录了模式串与主串(文本串)不匹配的时候，模式串应该从哪里开始重新匹配
# 前缀表用来 记录下标i之前（包括i）的字符串中，有多大长度的相同前缀后缀，比如上面的A和B
# B: aabaa的最大相等前后缀为aa
# 当目标到A的
#      ↓
# aabaabaafa

# B这个时候为
#      ↓
# aabaaf
# 发现不匹配了，那么只需要退回到最长相等(2)的前后缀的下一位到
#      ↓
# aabaabaafa
#   ↓
# aabaaf
# 继续匹配即可，因为A中箭头b前面的aa肯定是和b中箭头b前方的aa相等的，所以不用从头开始再次匹配

# @lc code=start
class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        nl = len(needle)
        if nl == 0:
            return 0

        next = self.getNext(needle)
        j, hl = 0, len(haystack)
        for i in range(hl):
            c = haystack[i]
            while j > 0 and c != needle[j]:  # 如果遇到不相等的，回到最大相同的前缀子串后继续匹配，如果还不想等在去找子串，直到 = 0
                j = next[j - 1]

            if needle[j] == c:
                j += 1

            if j >= nl:
                return i - j + 1

        return -1
    # 前缀: 第一个字符开始不包含最后一个字符的子串
    # 后缀: 第二个字符开始包含最后一个字符的子串，两者相同为最长相等前缀
    # 得到前缀表，aabaaf的可以表示为[0, 1, 0, 1, 2, 0], 每一位表示str[:i]有多大长度的相同前缀后缀, 记住回到的是前缀，所以这里长度=位置，查找的时候要回到位置的下一位继续进行匹配

    def getNext(self, s: str) -> list:
        j, next = 0, [0 for i in s]  # j同时代表下标也代表最大相等子串长度，所以[0, j]代表的是最大相等前后缀的前缀
        next[0] = j
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:  # 如果前后缀不一致了，回退, j > 0保证跳出环境，j = 0的时候证明到了第1位，就不用在回退了
                j = next[j - 1]

            if s[i] == s[j]:  # 如果一致，则给j + 1
                j += 1

            next[i] = j  # 给i位置赋值最大相等子串长度

        return next


# @lc code=end
if __name__ == '__main__':
    s = Solution()

    result = s.strStr("abcdefbadbaffcdbadbac", "badbac")
    print(result)
    result = s.strStr("aaaabbccbabba", "bba")
    print(result)
    result = s.strStr("hello", "ll")
    print(result)
    result = s.strStr("aaaaa", "")
    print(result)
    result = s.getNext("aaa")
    print(result)
