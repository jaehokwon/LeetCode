class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tile = set()
            
        def dfs(word, full):
            if word:
                tile.add(word)
            for i in range(len(full)):
                dfs(word + full[i], full[:i] + full[i+1:])
        
        dfs('', tiles)
        return len(tile)