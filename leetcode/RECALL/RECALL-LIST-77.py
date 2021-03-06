#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   RECALL-LIST-77.py
@Time    :   2021/09/14 14:09:47
@Author  :   Abel
'''


from typing import List


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []
        return self.backtracking(n, k, 1, path, result)

    def backtracking(self, n: int, k: int, start_index: int, path: list, result: list):
        if k == len(path):
            result.append(path[:])
            return

        for i in range(start_index, n + 1):
            path.append(i)
            self.backtracking(n, k, i + 1, path, result)
            path.pop(-1)

        return result


if __name__ == '__main__':
    s = Solution()
    n, k = 4, 2
    result = s.combine(n, k)
    print(result)
