# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # hi
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        output = []
        def dfs(root):
            if not root:
                output.append('#')
                output.append(",")
                return
            
            output.append(str(root.val))
            output.append(",")
            dfs(root.left)
            dfs(root.right)
            return
            
        dfs(root)
        result = "".join(output)
        return result
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        li = data.split(",")
        que = deque(li)
         
        def dfs():
            if not que:
                return

            cur_val = que.popleft()

            if cur_val == '#':
                return

            cur_node = TreeNode(int(cur_val))
            cur_node.left = dfs()
            cur_node.right = dfs()

            return cur_node

        return dfs()
                

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

