class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sumNumbers(self, root) -> int:
        ans = [0]
        def dfs(root,val):
            if not root:
                return

            if not root.left and not root.right:
                val+=str(root.val)
                ans[0]+=int(val)
            dfs(root.left,val+str(root.val))
            dfs(root.right,val+str(root.val))
        dfs(root,"")
        return ans[0]
root = TreeNode(4)
root.left = TreeNode(9)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)
root.right = TreeNode(0)
slt = Solution()
print(slt.sumNumbers(root))


