#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True

        que = deque()
        que.append(root.left)
        que.append(root.right)

        while que:
            # 只要连续的两个数值一样就是对称的，因为我们加入队列的顺序是按对称加入的
            nodeLeft, nodeRight = que.popleft(), que.popleft()
            if not nodeLeft and not nodeRight:  # 两个都位空也是对称的
                continue
            if not nodeLeft or not nodeRight:  # 只有一个为空，则不行
                return False
            if nodeLeft.val != nodeRight.val:
                return False
            # 对称加入各个节点
            que.append(nodeLeft.left)
            que.append(nodeRight.right)
            que.append(nodeLeft.right)
            que.append(nodeRight.left)

        return True


class Solution2:  # 草率了，一开始想层序遍历直接加结果，那样应该更好点，参考Solution1
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        que = deque()
        if root.left:
            que.append(root.left)
        if root.right:
            que.append(root.right)

        while que:
            size = len(que)
            if size % 2 != 0:
                return False

            for i in range(size // 2):
                nodeLeft, nodeRight = que.popleft(), que.popleft()

                if nodeLeft.val != nodeRight.val:
                    return False

                if nodeLeft.left and nodeRight.right:
                    que.append(nodeLeft.left)
                    que.append(nodeRight.right)
                elif not nodeRight.right and not nodeLeft.left:
                    pass
                else:
                    return False

                if nodeLeft.right and nodeRight.left:
                    que.append(nodeLeft.right)
                    que.append(nodeRight.left)
                elif not nodeLeft.right and not nodeRight.left:
                    pass
                else:
                    return False

        return True
# @lc code=end
