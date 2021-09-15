#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   RECALL-784.PY
@Time    :   2021/09/14 19:58:37
@Author  :   Abel
'''
from typing import List
import functools


class Solution:
    result = []

    def letterCasePermutation(self, s: str) -> List[str]:
        return self.backtracking(s, True, -1, '', [])

    def backtracking(self, s: str, lower: bool, index: int, path: str, result: List[str]):
        if index < len(s) and index >= 0:
            path += s[index].lower() if lower else s[index].upper()

        if len(path) == len(s):
            result.append(path[:])
            path = ''
            return

        # print(lower, index, path, result)
        if index < len(s) - 1:
            if s[index + 1].isdigit():
                self.backtracking(s, True, index + 1, path, result)
            else:
                print('===', lower, index, path, result)
                self.backtracking(s, True, index + 1, path, result)
                print('-=-', lower, index, path, result)
                self.backtracking(s, False, index + 1, path, result)
                print('---', lower, index, path, result)

        return result


if __name__ == '__main__':
    s = Solution()
    result = s.letterCasePermutation('a1b2')
    print(result)
