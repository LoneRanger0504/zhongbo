# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给定一个二叉树，返回它的 前序 遍历。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # (1)递归实现前序遍历
        # def preorder(root):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     if root.left:
        #         preorder(root.left)
        #     if root.right:
        #         preorder(root.right)
        # res = []
        # if not root:
        #     return res
        # preorder(root)
        # return res
        # (2)非递归实现，使用队列辅助，实现栈的功能，
        # 添加节点的时候先添加右子树，再添加左子树，取得时候取队列末尾元素
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            root = queue.pop(-1)
            res.append(root.val)
            if root.right:
                queue.append(root.right)
            if root.left:
                queue.append(root.left)
        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    solution = Solution()
    res = solution.preorderTraversal(root)
    print(res)
