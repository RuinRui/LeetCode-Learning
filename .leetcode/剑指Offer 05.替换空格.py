class Solution:
    def replaceSpace(self, s: str) -> str:
        return ''.join(['%20' if c == ' ' else c for c in s])


if __name__ == '__main__':
    s = Solution()
    result = s.replaceSpace("abc def gh")
    print(result)
