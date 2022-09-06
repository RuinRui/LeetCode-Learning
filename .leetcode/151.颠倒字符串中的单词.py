#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 颠倒字符串中的单词
#

# @lc code=start

class Solution:
    def reverseWords(self, s: str) -> str:
        words, word = [], []
        for c in s:
            if c == ' ' and len(word):
                words.append(word)
                word = word[:0]
            elif c != ' ':
                word.append(c)

        if len(word):
            words.append(word)

        ws = ''
        for i in range(len(words) - 1, -1, -1):
            ws += ''.join(words[i])
            if i != 0:
                ws += ' '

        return ws


# 参考代码随想录的思路，实际上内存是省了点，但是时间上被压倒了
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         # 删除头尾空格
#         l = len(s)
#         left, right = 0, l - 1
#         while left < l:
#             if s[left] == ' ':
#                 left += 1
#             else:
#                 break

#         while right > 0:
#             if s[right] == ' ':
#                 right -= 1
#             else:
#                 break

#         # 删除单词中间的多余空格
#         result = []
#         slow, fast = left, left
#         while slow <= right:
#             if s[slow] != ' ':
#                 result.append(s[slow])
#                 slow += 1
#             else:
#                 result.append(' ')
#                 fast = slow + 1
#                 while fast <= right and s[fast] == ' ':
#                     fast += 1
#                 slow = fast

#         # 翻转字符串
#         left, right = 0, len(result) - 1
#         while left < right:
#             result[left], result[right] = result[right], result[left]
#             left += 1
#             right -= 1

#         # 翻转单词
#         slow, fast = 0, 0
#         while fast <= len(result):
#             if fast == len(result) or result[fast] == ' ':
#                 # 翻转slow到fast - 1的字符
#                 left, right = slow, fast - 1
#                 while left < right:
#                     result[left], result[right] = result[right], result[left]
#                     left += 1
#                     right -= 1

#                 slow = fast + 1
#                 fast = slow

#             fast += 1

#         return ''.join(result)


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    result = s.reverseWords("    hello world  ")
    print(result)
    result = s.reverseWords("   the   sky   is   blue   ")
    print(result)
    result = s.reverseWords("a good   example")
    print(result)
