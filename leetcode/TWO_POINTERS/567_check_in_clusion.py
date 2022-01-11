#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   567_.py
@Time    :   2021/09/22 15:26:52
@Author  :   Abel
'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts = [0] * 26
        for i, c in enumerate(s1):
            counts[ord(c) - ord('a')] -= 1
            counts[ord(s2[i]) - ord('a')] += 1

        diff = 0
        for i in range(26):
            if counts[i] != 0:
                diff += 1

        if diff == 0:
            return True

        s1_l = len(s1)
        for i in range(s1_l, len(s2)):
            c = s2[i]
            out_i, in_i = ord(s2[i - s1_l]) - ord('a'), ord(s2[i]) - ord('a')
            if out_i == in_i:
                continue

            out_count, in_count = counts[out_i], counts[in_i]
            if out_count == 0:
                diff += 1

            counts[out_i] -= 1
            if counts[out_i] == 0:
                diff -= 1

            if in_count == 0:
                diff += 1

            counts[in_i] += 1
            if counts[in_i] == 0:
                diff -= 1

            if diff == 0:
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    s.checkInclusion('ab', 'eidbaooo')
