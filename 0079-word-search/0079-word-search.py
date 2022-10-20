class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])
        word_len = len(word)

        def search(x, y, i, flags) -> bool:
            flags[y][x] = 1

            if i == word_len:
                return True

            if y - 1 >= 0 and flags[y - 1][x] == 0 and board[y - 1][x] == word[i] and search(x, y - 1, i + 1, flags): # up
                return True
            if y + 1 < m and flags[y + 1][x] == 0 and board[y + 1][x] == word[i] and search(x, y + 1, i + 1, flags): # down
                return True
            if x - 1 >= 0 and flags[y][x - 1] == 0 and board[y][x - 1] == word[i] and search(x - 1, y, i + 1, flags): # left
                return True
            if x + 1 < n and flags[y][x + 1] == 0 and board[y][x + 1] == word[i] and search(x + 1, y, i + 1, flags): # right
                return True
            
            flags[y][x] = 0

            return False

        
        for y in range(0, m):
            for x in range(0, n):
                if board[y][x] == word[0] and search(x, y, 1, [[0 for _ in range(0, n)] for _ in range(0, m)]):
                    return True

        return False
