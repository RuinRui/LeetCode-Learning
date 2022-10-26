#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:  # 优化写法
    def simplifyPath(self, path: str) -> str:
        arr = []
        components = path.split('/')
        # 直接得到各个文件(夹)名
        for c in components:
            if c == '':
                continue

            if c == '.':  # 当前目录，不用动
                continue
            elif c == '..':  # 上一级目录，pop最后的文件(夹)
                if arr:
                    arr.pop()
                continue
            arr.append(c)

        # 文件(夹)中间加上/
        return '/' + '/'.join(arr)


class Solution2:
    def simplifyPath(self, path: str) -> str:
        arr = []
        components = path.split('/')

        for c in components:
            if c != '':
                arr.append(c)

            if arr and arr[-1] == '/':
                continue
            arr.append('/')

        result = []
        for c in arr:
            if c == '.':
                if result and result[-1] == '/':
                    result.pop()
                continue
            elif c == '/':
                if result and result[-1] == '/':
                    continue
            elif c == '..':
                if result:
                    result.pop()
                if result:
                    result.pop()
                continue

            result.append(c)

        if len(result) > 1 and result[-1] == '/':
            result.pop()
        return ''.join(result)


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    result = s.simplifyPath('/home/')
    print(result)
    result = s.simplifyPath('/../')
    print(result)
    result = s.simplifyPath('/home//foo/')
    print(result)
    result = s.simplifyPath('/a/./b/../../c/')
    print(result)
