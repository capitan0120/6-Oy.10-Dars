# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def toList(r1,stk):
            if not(r1): return
            stk.append(r1.val)
            toList(r1.left,stk)
            toList(r1.right,stk)
            return stk
        treeNodes = toList(root,[])
        ans = []
        if treeNodes:
            for e in treeNodes:
                for e2 in treeNodes:
                    if e != e2:
                        ans.append(abs(e-e2))
        print(treeNodes)
        if ans:
            return min(ans)
        else:
            return 0