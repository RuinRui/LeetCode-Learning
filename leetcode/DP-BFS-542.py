#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   DP|BFS-542.PY
@Time    :   2021/09/13 10:49:58
@Author  :   Abel
'''
import collections
from typing import List, Sequence
import time


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dist = [[10**9] * n for _ in range(m)]
        # 从右上到左下
        for x in range(m - 1, -1, -1):
            for y in range(n):
                if mat[x][y] == 0:
                    dist[x][y] = 0
                    continue

                if x < m - 1:
                    dist[x][y] = min(dist[x][y], dist[x + 1][y] + 1)
                if y > 0:
                    dist[x][y] = min(dist[x][y], dist[x][y - 1] + 1)
        # 从左下到右上
        for x in range(m):
            for y in range(n - 1, -1, -1):
                if mat[x][y] == 0:
                    dist[x][y] = 0
                    continue

                if x > 0:
                    dist[x][y] = min(dist[x][y], dist[x - 1][y] + 1)
                if y < n - 1:
                    dist[x][y] = min(dist[x][y], dist[x][y + 1] + 1)
        return dist

    # DP 动态规划
    def updateMatrix2(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dist = [[10**9] * n for _ in range(m)]
        # 从左上到右下
        for x in range(m):
            for y in range(n):
                if mat[x][y] == 0:
                    dist[x][y] = 0
                    continue

                if x > 0:
                    dist[x][y] = min(dist[x][y], dist[x - 1][y] + 1)
                if y > 0:
                    dist[x][y] = min(dist[x][y], dist[x][y - 1] + 1)
        # 从右下到左上
        for x in range(m - 1, -1, -1):
            for y in range(n - 1, -1, -1):
                if mat[x][y] == 0:
                    dist[x][y] = 0
                    continue

                if x < m - 1:
                    dist[x][y] = min(dist[x][y], dist[x + 1][y] + 1)
                if y < n - 1:
                    dist[x][y] = min(dist[x][y], dist[x][y + 1] + 1)
        return dist

    # BFS

    def updateMatrix1(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        result = [[0] * n for i in range(m)]
        seed = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]
        que = collections.deque(seed)
        searched = set(seed)

        while que:
            x, y = que.popleft()
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                tx, ty = dx + x, dy + y
                if tx >= 0 and tx < m and ty >= 0 and ty < n and (tx, ty) not in searched:
                    result[tx][ty] = result[x][y] + 1
                    que.append((tx, ty))
                    searched.add((tx, ty))

        return result


if __name__ == '__main__':
    s = Solution()
    start = time.time()
    mat = [[0, 1, 1, 0, 0],
           [0, 1, 1, 0, 0],
           [0, 1, 0, 0, 1],
           [1, 1, 1, 1, 0],
           [1, 0, 0, 1, 0]]
    result = s.updateMatrix(mat)
    print(result)
    print('time ===== %f' % (time.time() - start))
