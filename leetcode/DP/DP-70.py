#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   DP-70.py
@Time    :   2021/09/14 15:44:08
@Author  :   Abel
'''

import functools


class Solution:
    @functools.lru_cache(100)
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return self.climbStairs(1) + self.climbStairs(0)

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == '__main__':
    s = Solution()
    for i in range(1, 40):
        print(s.climbStairs(i))
