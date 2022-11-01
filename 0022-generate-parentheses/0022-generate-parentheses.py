class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.dfs(n, 1, 0, '(', result)
        return result
    
    def dfs(self, n, i, j, cur_str, lst):
        if i < j or i > n or j > n:
            return

        if n == i == j:
            lst.append(cur_str)
            return
        
        self.dfs(n, i+1, j, cur_str + '(', lst)
        self.dfs(n, i, j+1, cur_str + ')', lst)
