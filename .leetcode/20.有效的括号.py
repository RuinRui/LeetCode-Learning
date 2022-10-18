#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif not stack or stack[-1] != c:
                return False
            else:
                stack.pop()

        return True if not stack else False


class Solution2:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        arr = [c for c in s]
        data = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        index = 1
        while index < len(arr) and len(arr) > 0:
            c = arr[index]
            if c in data and index > 0 and arr[index - 1] == data[c]:
                del arr[index]
                del arr[index - 1]
                index -= 2
            index += 1

        return True if len(arr) == 0 else False


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    result = s.isValid("()[]{}")
    print(result)
    result = s.isValid("()")
    print(result)
    result = s.isValid("(]")
    print(result)
    result = s.isValid("([{}][()])")
    print(result)
    result = s.isValid("{[]}")
    print(result)
    result = s.isValid("[([]])")
    print(result)
