# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/ti-huan-kong-ge-lcof/
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

class Solution:
    def replaceSpace(self, s: str) -> str:
        return ''.join(['%20' if c == ' ' else c for c in s])


if __name__ == '__main__':
    s = Solution()
    result = s.replaceSpace("abc def gh")
    print(result)
