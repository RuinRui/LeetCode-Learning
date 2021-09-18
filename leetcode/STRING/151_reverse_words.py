#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   reverse_words_151.py
@Time    :   2021/09/18 11:03:03
@Author  :   Abel

给你一个字符串 s ，逐个翻转字符串中的所有 单词 。

单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。

请你返回一个翻转 s 中单词顺序并用单个空格相连的字符串。

说明：

输入字符串 s 可以在前面、后面或者单词间包含多余的空格。
翻转后单词间应当仅用一个空格分隔。
翻转后的字符串中不应包含额外的空格。
 

示例 1：
输入：s = "the sky is blue"
输出："blue is sky the"

示例 2：
输入：s = "  hello world  "
输出："world hello"
解释：输入字符串可以在前面或者后面包含多余的空格，但是翻转后的字符不能包括。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def reverseWords(self, s: str) -> str:
        result, i, word = [], 0, ''

        while i < len(s):
            if s[i] == ' ' and len(word) > 0:
                result.insert(0, word)
                word = ''
            elif s[i] != ' ':
                word += s[i]
            i += 1

        if word:
            result.insert(0, word)

        return ' '.join(result)


if __name__ == '__main__':
    s = Solution()
    mat = ['the sky is blue', "  hello world  "]
    for m in mat:
        print(s.reverseWords(m))
