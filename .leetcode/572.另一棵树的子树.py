#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # 解法1：实在不像个简单题啊，每一次到root的一个节点时都去和subroot对比一次，时间复杂度就是root的节点数 * subroot的节点数
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(pNode: Optional[TreeNode], qNode: Optional[TreeNode]) -> bool:
            if not pNode and not qNode:
                return True
            if (not qNode and pNode) or (not pNode and qNode) or qNode.val != pNode.val:
                return False

            return check(pNode.left, qNode.left) and check(pNode.right, qNode.right)

        def dfs(pNode: Optional[TreeNode], qNode: Optional[TreeNode]) -> bool:
            if not pNode:
                return False
            return check(pNode, qNode) or dfs(pNode.left, qNode) or dfs(pNode.right, qNode)

        return dfs(root, subRoot)


class Solution2:  # 解法2：把一棵树数字化，用一个值代替空节点，然后比较两个数组，可以使用leetcode.28题里的KMP算法来快速的比较subroot的数组是否是root的子数组
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 遍历行成树的数组
        def centerOrder(root: Optional[TreeNode], result: List[int]):
            if not root:
                result.append(-10**5)
                return
            result.append(root.val)
            centerOrder(root.left)
            centerOrder(root.right)
            return

        rootArr, subArr = [], []
        centerOrder(root, rootArr)
        centerOrder(root, subArr)
        # 获取要在rootArr中查找的subArr的next数组
        next = self.getNextArr(subArr)
        i, j, l = 0, 0, len(subArr)
        for r in range(rootArr):
            while j > 0 and r != subArr[j]:
                j = next[j - 1]

            if r == subArr[j]:
                j += 1

            if j >= l:
                return True

        return False

    # KMP算法获取next数组
    def getNextArr(self, arr: List[int]) -> List[int]:
        j, next = 0, [0 for i in arr]
        for i in range(len(arr)):
            while j > 0 and arr[j] != arr[i]:
                j = next[i - 1]

            if arr[j] == arr[i]:
                j += 1

            next[i] = j

# @lc code=end
