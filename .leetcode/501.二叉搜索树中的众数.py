#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
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
    """
    解法1: 遍历二叉树,弄个map存储次数,较为简单,此处略
    解法2: 和其他的一样,充分利用二叉搜索树的特性,既然是顺序排列,那以前后数字不一样的地方开始统计两种数字的出现频率,保留最大值和下一种数字频率作比较就行
    """

    def __init__(self) -> None:
        self.topNums = []
        self.numCount = 0
        self.maxCount = 0
        self.node = None

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def findTopNum(root: Optional[TreeNode]) -> List[int]:
            if not root:
                return None

            findTopNum(root.left)
            if root.val == self.node.val:
                self.numCount += 1
            else:
                self.numCount = 1
                self.node = root

            if self.numCount == self.maxCount:
                self.topNums.append(self.node)

            if self.numCount > self.maxCount:
                self.maxCount = self.numCount
                self.topNums.clear()
                self.topNums.append(self.node)

            findTopNum(root.right)
            return self.topNums
        self.node = root
        return [t.val for t in findTopNum(root)]
# @lc code=end
