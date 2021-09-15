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

# 617 合并二叉树


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root2.right, root2.right)

        return merged


def prepare_parser():
    parser = argparse.ArgumentParser(description='arithmetic tools.')
    parser.add_argument('-n', '--prob_num', type=int, default=695, help='problem num')

    return parser


if __name__ == '__main__':
    parser = prepare_parser()
    args = parser.parse_args()

    s = Solution()
