#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   one.py
@Time    :   2021/09/09 15:22:17
@Author  :   Abel
'''
from typing import List
import collections
import argparse


# 733. 油漆桶功能
class Solution:
    c_image = list()
    o_color = 0

    # 解法1 DFS
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.c_image = image
        self.o_color = image[sr][sc]

        return self.depth_search(sr, sc, newColor, image, "上") or self.c_image

    def depth_search(self, x, y, new_color, image, dir) -> List[List[int]]:
        if x < 0 or y < 0 or x > len(image) - 1 or y > len(image[0]) - 1:
            return
        print(x, y)
        if self.c_image[x][y] == new_color or image[x][y] != self.o_color:
            return

        self.c_image[x][y] = new_color
        # 遍历上左下右
        self.depth_search(x, y+1, new_color, image, "上")
        self.depth_search(x-1, y, new_color, image, "左")
        self.depth_search(x+1, y, new_color, image, "右")
        self.depth_search(x, y-1, new_color, image, "下")

        return self.c_image

    # 解法2 BFS
    def floodFill1(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        current_color = image[sr][sc]
        if current_color == newColor:
            return image

        max_x = len(image)
        max_y = len(image[sr])
        que = collections.deque([(sr, sc)])
        while que:
            x, y = que.popleft()
            for mx, my in [(x, y + 1), (x-1, y), (x, y - 1), (x - 1, y)]:
                if mx >= 0 and my >= 0 and mx < max_x and my < max_y and image[mx][my] != newColor:
                    que.append((mx, my))
                    image[mx][my] = newColor

        return image


def prepare_parser():
    parser = argparse.ArgumentParser(description='arithmetic tools.')
    parser.add_argument('-n', '--prob_num', type=int, default=695, help='problem num')

    return parser


if __name__ == '__main__':
    parser = prepare_parser()
    args = parser.parse_args()

    s = Solution()
    prob_num = args.prob_num
    result = s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
    print(result)
