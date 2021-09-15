#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   LIST-POINTER-59.py
@Time    :   2021/09/15 14:42:44
@Author  :   Abel

给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

'''

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]
        # 右 下 左 上 1 2 3 4, (x,y)是坐标，以左上为起点
        direct, x, y, num = 1, -1, 0, 0
        right, down, left, up = n - 1, n - 1, 0, 0
        for i in range(n):
            for j in range(n):
                num += 1
                if direct == 1:  # 右
                    if x < right:
                        x += 1
                    else:
                        up += 1
                        y += 1
                        direct = 2
                elif direct == 2:  # 下
                    if y < down:
                        y += 1
                    else:
                        right -= 1
                        x -= 1
                        direct = 3
                elif direct == 3:  # 左
                    if x > left:
                        x -= 1
                    else:
                        down -= 1
                        y -= 1
                        direct = 4
                else:  # 上
                    if y > up:
                        y -= 1
                    else:
                        left += 1
                        x += 1
                        direct = 1
                result[y][x] = num

        return result


if __name__ == '__main__':
    s = Solution()
    targets = [3, 1, 20]
    for num in targets:
        print(s.generateMatrix(num))
