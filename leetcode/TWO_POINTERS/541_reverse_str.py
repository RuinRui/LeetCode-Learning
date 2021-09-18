#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   reverse_str.py
@Time    :   2021/09/18 10:01:55
@Author  :   Abel

给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
 
示例 1：
输入：s = "abcdefg", k = 2
输出："bacdfeg"

示例 2：
输入：s = "abcd", k = 2
输出："bacd"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-string-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        length = len(s)
        result = list(s)
        for start in range(0, length, 2 * k):
            left = start
            will_right = start + k - 1
            right = will_right if will_right < length else length - 1
            while left < right:
                temp = result[right]
                result[right] = result[left]
                result[left] = temp
                left += 1
                right -= 1

        return ''.join(result)


if __name__ == '__main__':
    s = Solution()
    mat = [('abcdefg', 2), ('abcd', 2), ('a', 2)]
    for m in mat:
        print(s.reverseStr(m[0], m[1]))
