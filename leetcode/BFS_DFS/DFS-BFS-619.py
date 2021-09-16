#!.venv/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   DFS|BFS-619.py
@Time    :   2021/09/10 14:23:43
@Author  :   Abel
'''
from typing import List
import collections
import argparse


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # 递归
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root

    # 层次遍历
    def connect1(self, root: 'Node') -> 'Node':
        if not root:
            return root

        que = collections.deque([root])
        while que:
            size = len(que)
            for i in range(size):
                node = que.popleft()

                if i < size - 1:
                    node.next = que[0]

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

        return root


def prepare_parser():
    parser = argparse.ArgumentParser(description='arithmetic tools.')
    parser.add_argument('-n', '--prob_num', type=int, default=695, help='problem num')

    return parser


if __name__ == '__main__':
    parser = prepare_parser()
    args = parser.parse_args()

    s = Solution()
