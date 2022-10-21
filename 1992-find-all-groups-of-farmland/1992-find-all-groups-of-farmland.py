class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = []

        for m in range(len(land)):
            for n in range(len(land[0])):
                if land[m][n] == 1:
                    res.append(self.dfs(land, m, n, []))

        return res
    
    def dfs(self, land, m, n, visitor) -> List[int]:
        if len(visitor) == 0:
            visitor = [m, n, m, n]
        elif m >= visitor[2] and n >= visitor[3]:
            visitor[2], visitor[3] = m, n
        
        land[m][n] = -1

        direction = [(1, 0), (0, 1)]

        for (n2, m2) in direction:
            if m+m2 < len(land) and n+n2 < len(land[0]) and land[m+m2][n+n2] == 1:
                visitor = self.dfs(land, m + m2, n + n2, visitor)
        
        return visitor