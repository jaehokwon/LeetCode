# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        graph = defaultdict(list)
        
        def dfs(node, parent=None):
            if node:
                if parent:
                    graph[node].append(parent)
                    graph[parent].append(node)
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root)
        
        leafs = []
        for node in graph.keys():
            if not node.left and not node.right:
                leafs.append(node)
        
        count = 0
        for leaf in leafs:
            queue = [(leaf, 0)]
            seen = set(queue)
            while queue:
                node, length = queue.pop(0)
                if length>distance:
                    break
                for node2 in graph[node]:
                    if node2 not in seen:
                        seen.add(node2)
                        queue.append((node2, length+1))
                if leaf!=node and node in leafs and length<=distance:
                    count+=1
        
        return count//2