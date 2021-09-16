#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   HASH_202.PY
@Time    :   2021/09/16 20:14:05
@Author  :   Abel
'''
import time


class Solution:
    def isHappy(self, n: int) -> bool:
        sum, split = 0, n
        showed = set([n])
        while split != 1:
            while split > 0:
                cs = split % 10
                split //= 10
                sum += cs**2
            split, sum = sum, 0

            if split in showed:
                return False

            showed.add(split)

        return True


if __name__ == '__main__':
    s = Solution()
    s.isHappy(2)
