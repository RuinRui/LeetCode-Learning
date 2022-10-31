#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

from collections import deque
from typing import List, Optional
# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result, st = [], deque()
        if not root:
            return result
        st.append(root)
        while st:
            levelResult = []
            for i in range(len(st)):  # 根据st长度遍历这一层节点
                node = st.popleft()
                levelResult.append(node.val)  # 这一层的每一个节点都存起来
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
            result.append(levelResult)

        return result


class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result, st = [], []
        if not root:
            return result
        st.append(root)
        while st:
            levelResult = []
            levelst = []
            while st:
                node = st.pop(0)
                levelResult.append(node.val)  # 这一层的每一个节点都存起来
                if node.left:
                    levelst.append(node.left)
                if node.right:
                    levelst.append(node.right)
            st.extend(levelst)  # 把这一层的所有节点都加进来
            result.append(levelResult)

        return result
# @lc code=end
