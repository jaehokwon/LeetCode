class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a = []
        self.dp(n, 1, 0, '(', a)
        return a
    
    def dp(self, n, i, j, cur_str, lst):
        if i < j or i > n or j > n:
            return

        if n == i == j:
            if cur_str not in lst:
                lst.append(cur_str)
            return
        
        self.dp(n, i+1, j, cur_str + '(', lst)
        self.dp(n, i, j+1, cur_str + ')', lst)