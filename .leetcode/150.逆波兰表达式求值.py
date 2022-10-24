#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

from typing import List
# @lc code=start


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        for c in tokens:
            if c == '+':
                a, b = arr.pop(), arr.pop()
                arr.append(a + b)
            elif c == '-':
                a, b = arr.pop(), arr.pop()
                arr.append(b - a)
            elif c == '*':
                a, b = arr.pop(), arr.pop()
                arr.append(a * b)
            elif c == '/':
                a, b = arr.pop(), arr.pop()
                arr.append(int(b / a))
            else:
                arr.append(int(c))

        return arr[0]


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    result = s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    print(result)
    result = s.evalRPN(["2", "1", "+", "3", "*"])
    print(result)
    result = s.evalRPN(["4", "3", "-"])
    print(result)
