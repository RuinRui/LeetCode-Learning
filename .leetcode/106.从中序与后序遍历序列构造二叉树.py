#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 如果为空数组，则为空节点
        if len(inorder) == 0:
            return None
        # 取后序遍历(左右中)的最后一个节点作为分割点，这个点就是中间节点
        center = postorder[-1]
        node = TreeNode(center)
        if len(inorder) == 1:
            return node
        # 把前序遍历分割成左右数组
        index = inorder.index(center)
        leftInorder = inorder[:index]
        rightInorder = inorder[index + 1:]
        # 把后续遍历分割成左右数组
        length = len(leftInorder)
        leftPostorder = postorder[:length]
        rightPostorder = postorder[length:-1]

        node.left = self.buildTree(leftInorder, leftPostorder)
        node.right = self.buildTree(rightInorder, rightPostorder)
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
    result = s.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    result = s.preorderTraversal(result)
    print('result >>> ', result)
