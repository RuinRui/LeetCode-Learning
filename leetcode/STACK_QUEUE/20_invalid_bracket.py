#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   20_invalid_bracket.py
@Time    :   2021/09/18 15:11:43
@Author  :   Abel

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
 
示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        dic = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        for c in s:
            if c == '}' or c == ']' or c == ')':
                if not result or result[-1] != dic[c]:
                    return False
                result.pop()
            else:
                result.append(c)

        return not result


if __name__ == '__main__':
    s = Solution()
    mat = ["()[]{}", "([)]", "(]", "{[]}", "()", "]", "{{]"]
    for m in mat:
        print(s.isValid(m))
