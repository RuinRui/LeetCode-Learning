#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   150_eval_rpn.py
@Time    :   2021/09/18 16:48:47
@Author  :   Abel
'''

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbol = ['+', '-', '*', '/']
        for n in tokens:
            if n in symbol:
                s1 = int(stack.pop())
                s2 = int(stack.pop())
                res = 0
                if n == '+':
                    res = s1 + s2
                elif n == '-':
                    res = s2 - s1
                elif n == '*':
                    res = s2 * s1
                else:
                    res = int(s2 / s1)

                stack.append(res)
            else:
                stack.append(n)

        return stack.pop()


if __name__ == '__main__':
    s = Solution()
    mat = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], ["4", "13", "5", "/", "+"]]
    for m in mat:
        print(s.evalRPN(m))
