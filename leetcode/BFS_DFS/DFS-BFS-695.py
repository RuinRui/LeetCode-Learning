#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   one.py
@Time    :   2021/09/10 15:22:17
@Author  :   Abel
'''
from typing import List
import collections
import argparse

# 695 岛屿的最大面积


class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:  # 改进解法2 BFS
        if not grid:
            return 0

        que = collections.deque()
        max_area = 0

        for x, rows in enumerate(grid):  # 遍历每个点
            for y, col in enumerate(rows):
                if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] != 1:  # BFS要保证在循环中只加入能搜索到陆地的点，否则就continue
                    continue
                grid[x][y] = 0
                que.appendleft((x, y))
                cur_area = 1
                while que:
                    x, y = que.popleft()
                    for mx, my in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        next_x, next_y = x + mx, y + my
                        # BFS要保证在循环中只加入能搜索到陆地的点，否则就continue
                        if next_x < 0 or next_y < 0 or next_x == len(grid) or next_y == len(grid[0]) or grid[next_x][next_y] != 1:
                            continue
                        que.appendleft((next_x, next_y))
                        grid[next_x][next_y] = 0
                        cur_area += 1
                max_area = max(max_area, cur_area)

        return max_area

    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:  # 改进解法1 DFS
        if not grid:
            return 0

        max_area = 0
        for x, rows in enumerate(grid):
            for y, col in enumerate(rows):
                max_area = max(self.depth_search(grid, x, y), max_area)

        return max_area

    def depth_search(self, grid, x, y) -> int:
        # 遇到越界的或者已经搜索过的或者是水的则返回0
        if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] != 1:
            return 0

        grid[x][y] = 0
        count = 1  # 找到了陆地，则继续遍历陆地的相邻节点，相邻节点如果是陆地也会寻找周围节点，周而复始，直到一个点的四周全是水则开始返回，这时候他的父节点会计算以自己为节点的发起的搜索一共有多少陆地。一直到最上层。
        for mx, my in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            count += self.depth_search(grid, x + mx, y + my)

        return count

    def maxAreaOfIsland1(self, grid: List[List[int]]) -> int:  # 自创解法ಥ_ಥ
        # 只要有一个点的上下左右有1(除了已知的点)就可以一直搜索下去
        # 已搜过的点表示为2
        # 如果一个循环之后没有1则count + 1
        if not grid:
            return 0

        has_no_lands_points = []
        has_land, land, land_count, max_land_area, current_land_area = False, 1, 0, 0, 0
        already_search = 2
        max_x, max_y = len(grid), len(grid[0])
        que = collections.deque([(0, 0)])

        if grid[0][0] == 1:
            has_land = True
            max_land_area = 1
            current_land_area = 1
        grid[0][0] = already_search

        # 如果一个有陆地的点周围都没有陆地，则该点搜索结束，以此内推，当结束的点=有陆地的点时
        while que:
            x, y = que.popleft()
            for mx, my in [(x-1, y),  (x+1, y), (x, y + 1), (x, y - 1)]:
                if mx < max_x and mx >= 0 and my < max_y and my >= 0 and grid[mx][my] != already_search:
                    if grid[mx][my] == land:  # 出现陆地继续搜这个点接壤的
                        if not has_land:
                            current_land_area = 0
                            print('----------陆地分割线----------', que)
                        if len(que) and not has_land:  # 之前搜的是没有陆地的点时这时候要首先搜索陆地点，搜完再搜no_lands
                            has_no_lands_points.extend(que)
                            que.clear()
                        que.appendleft((mx, my))
                        current_land_area += 1
                        grid[mx][my] = already_search
                        print('发现land ---> ', mx, my, que)
                        if not has_land:
                            has_land = True
                            break
                        has_land = True
                    else:
                        has_no_lands_points.append((mx, my))
                    grid[mx][my] = already_search

            # 如果已经没有可搜寻的点了并且有陆地, 则表明这是一块陆地了
            if not que:
                print("empty que ", has_land, has_no_lands_points)
                if has_land:
                    has_land = False
                    land_count += 1
                    if current_land_area > max_land_area:
                        max_land_area = current_land_area
                # 把那些没陆地的点加入搜索中
                que.extend(has_no_lands_points[:])
                has_no_lands_points.clear()

        return max_land_area


def prepare_parser():
    parser = argparse.ArgumentParser(description='arithmetic tools.')
    parser.add_argument('-n', '--prob_num', type=int, default=695, help='problem num')

    return parser


if __name__ == '__main__':
    parser = prepare_parser()
    args = parser.parse_args()

    s = Solution()
    for grid in [[[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]], [[0, 1], [1, 0]], [[1]], [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                                                                                                 [0, 0, 0, 0, 0, 0, 0,
                                                                                                                     1, 1, 1, 0, 0, 0],
                                                                                                                 [0, 1, 1, 0, 1, 0, 0,
                                                                                                                     0, 0, 0, 0, 0, 0],
                                                                                                                 [0, 1, 0, 0, 1, 1, 0,
                                                                                                                     0, 1, 0, 1, 0, 0],
                                                                                                                 [0, 1, 0, 0, 1, 1, 0,
                                                                                                                     0, 1, 1, 1, 0, 0],
                                                                                                                 [0, 0, 0, 0, 0, 0, 0,
                                                                                                                     0, 0, 0, 1, 0, 0],
                                                                                                                 [0, 0, 0, 0, 0, 0, 0,
                                                                                                                     1, 1, 1, 0, 0, 0],
                                                                                                                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]]:
        result = s.maxAreaOfIsland(grid)
        print('max area === ', result)

    print(result)
