# 来源：力扣（LeetCode）
# 链接：https: // leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

class Solution:
    # 现在n变成 1 <= n < s.length <= 10000
    # 所以可以直接化为 return ''.join(s[n:] + s[:n]), 送分题
    def reverseLeftWords(self, s: str, n: int) -> str:
        moveCount = n % len(s)
        result = s[moveCount:] + s[:moveCount]
        return ''.join(result)


if __name__ == '__main__':
    s = Solution()
    result = s.reverseLeftWords("abc def gh", 13)
    print(result)
    result = s.reverseLeftWords("abcdefg", 2)
    print(result)
