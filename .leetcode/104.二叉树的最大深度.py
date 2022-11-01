#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
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

# 如何理解递归
# 这里的递归法一定要搞明白 递归中会把临时变量压栈，等递归回来后这些变量会弹出栈，如果递归中只是改变了临时变量，那么递归回来时这些临时变量就被丢弃了，所以如果想保存递归中的临时变量，要么用被函数外引用的指针变量，比如数组，或者把临时变量返回，递归回来时接受这个临时变量


class Solution:  # 最好用最符合逻辑的是层序遍历
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        st, depth = deque(), 0
        if not root:
            return depth

        st.append(root)
        while st:
            size = len(st)
            depth += 1
            for i in range(size):
                node = st.popleft()
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)

        return depth


class Solution3:  # 前序遍历
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def digDeep(node: Optional[TreeNode], deep: int, maxDepth: int) -> int:
            maxDepth = deep if deep > maxDepth else maxDepth

            if node.left:
                maxDepth = digDeep(node.left, deep + 1, maxDepth)
            if node.right:
                maxDepth = digDeep(node.right, deep + 1, maxDepth)

            return maxDepth

        return digDeep(root, 1, 0)


class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def digDeep(node: Optional[TreeNode], deep: int, maxDepth: int) -> int:
            if not node:
                if deep > maxDepth:
                    maxDepth = deep
                return maxDepth
            deep += 1
            # 保留上一个节点的深度，留给右侧的遍历用
            tmpDeep = deep
            maxDepth = digDeep(node.left, deep, maxDepth)
            maxDepth = digDeep(node.right, tmpDeep, maxDepth)
            return maxDepth

        return digDeep(root, 0, 0)
# @lc code=end
