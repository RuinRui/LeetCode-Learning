#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   BFS-994.py
@Time    :   2021/09/13 17:13:51
@Author  :   Abel
@Title  :   腐烂的桔子
'''
from typing import List
import collections
import time


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 找出被隔离的橘子和统计新鲜的橘子
        m, n = len(grid), len(grid[0])
        fresh, rot = 0, []
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 2:
                    rot.append((x, y))
                elif grid[x][y] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        if len(rot) == 0:
            return -1

        minutes, rotfruit = 0, 0
        que = collections.deque(rot)
        rot.clear()
        while que:
            tx, ty = que.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = tx + dx, ty + dy
                if x < 0 or y < 0 or x > m - 1 or y > n - 1 or grid[x][y] == 2:  # 越界或腐烂的橘子就不查了
                    continue

                if grid[x][y] == 1:
                    grid[x][y] = 2
                    rot.append((x, y))
                    rotfruit += 1

            if not que:  # 过去的分钟数
                minutes += 1
                if rotfruit == fresh:
                    return minutes

                if not len(rot):
                    return -1
                que = collections.deque(rot)
                rot.clear()


if __name__ == '__main__':
    s = Solution()
    start = time.time()
    mat = [[[2], [2], [1], [0], [1], [1]],
           [[1], [2], [0]],
           [[2, 1, 1], [1, 1, 0], [0, 1, 1]],
           [[2, 1, 1], [0, 1, 1], [1, 0, 1]],
           [[0, 2]],
           [[0]],
           [[1]],
           [[0, 0, 0, 0]]]
    for m in mat:
        result = s.orangesRotting(m)
        print('spend time === %f oranges rot time === %d' % (time.time() - start, result))
