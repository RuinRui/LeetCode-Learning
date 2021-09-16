#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   Hash242.py
@Time    :   2021/09/16 17:31:31
@Author  :   Abel

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-anagram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


from typing import Counter


class Solution:
    # 骚操作
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

    # 骚操作
    def isAnagram_3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)

    def isAnagram_2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        l = [0 for _ in range(26)]
        diff = 0
        for i in range(len(s)):
            cs, ct = s[i], t[i]
            sindex = ord(cs) - ord('a')
            tindex = ord(ct) - ord('a')

            if l[sindex] == 0:
                diff += 1
            if l[tindex] == 0 and sindex != tindex:
                diff += 1

            l[sindex] += 1
            l[tindex] -= 1

            if l[sindex] == 0:
                diff -= 1
            if l[tindex] == 0 and sindex != tindex:
                diff -= 1

        return False if diff else True

    def isAnagram_1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set()
        dic, diff = {}, 0
        for c in s:
            if c not in dic:
                dic[c] = 1
                diff += 1
            else:
                dic[c] += 1

        for c in t:
            if c not in dic:
                return False
            else:
                dic[c] -= 1
                if dic[c] == 0:
                    diff -= 1

        return False if diff else True
