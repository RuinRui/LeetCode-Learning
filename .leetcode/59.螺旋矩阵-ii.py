#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
from typing import List
# @lc code=start


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for i in range(n)]
        left, right, top, bottom = 0, n-1, 0, n-1
        i, j, k, d = 0, 0, 0, 1
        while k < n * n:
            matrix[j][i] = k + 1
            if k == n * n - 1:  # 处理边界条件，因为k == n * n  - 1时到最后一个点了，还想换方向，这时候边界条件已经是right < left and top > bottom了
                break

            if i < right and d == 1:  # 向右
                i += 1
            elif j < bottom and d == 2:  # 向下
                j += 1
            elif i > left and d == 3:  # 向左
                i -= 1
            elif j > top and d == 0:  # 向上
                j -= 1
            else:  # 改变方向
                if d == 1:
                    top += 1
                elif d == 2:
                    right -= 1
                elif d == 3:
                    bottom -= 1
                elif d == 0:
                    left += 1
                d = (d + 1) % 4
                k -= 1  # 因为这里其实没有赋值，等于一个k被浪费了，所以要减一下
            k += 1

        return matrix
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    result = s.generateMatrix(1)
    print(result)
