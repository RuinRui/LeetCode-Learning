#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        sumSet = set()
        sum, remainder = 0, 0
        while 1:
            while n:
                remainder = n % 10
                n = n // 10
                sum += remainder * remainder

            if sum == 1:
                return True
            if sum in sumSet:
                return False
            sumSet.add(sum)
            n, sum = sum, 0

        return True


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    result = s.isHappy(2)
    print(result)
