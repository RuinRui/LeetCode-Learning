#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        # 前序的第一个节点必定是中间节点
        center = preorder[0]
        node = TreeNode(center)
        if len(preorder) == 1:
            return node

        # 把中序遍历用中间节点分开，同106题
        index = inorder.index(center)
        leftInorder = inorder[:index]
        rightInorder = inorder[index + 1:]
        # 同样拆分前序遍历
        length = len(leftInorder)
        leftPreorder = preorder[1:1+length]
        rightPreorder = preorder[1+length:]

        node.left = self.buildTree(leftPreorder, leftInorder)
        node.right = self.buildTree(rightPreorder, rightInorder)

        return node

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes, result = [], []
        if not root:
            return result

        nodes.append(root)
        while nodes:
            node = nodes.pop()
            result.append(node.val)
            if node.right:
                nodes.append(node.right)
            if node.left:
                nodes.append(node.left)

        return result


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    result = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    result = s.preorderTraversal(result)
    print('result >>> ', result)
