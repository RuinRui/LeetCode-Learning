#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   3_max_norepeat_str.py
@Time    :   2021/12/30 11:06:42
@Author  :   Abel
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, occ, count, ans = 0, 0, set(), 0, 0
        for i, c in enumerate(s):
            right = i
            if c not in occ:
                occ.add(c)
            else:
                ans = max(len(occ), ans)
                while c in occ and left < right:
                    occ.remove(s[left])
                    left += 1
                occ.add(c)

            ans = max(len(occ), ans)

        return ans


if __name__ == '__main__':
    s = Solution()
    s.lengthOfLongestSubstring("abcabcbb")
