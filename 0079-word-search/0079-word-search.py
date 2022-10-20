class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        word_len = len(word)

        # compare board, word char count
        board_dict = defaultdict(int)
        for y in range(m):
            for x in range(n):
                board_dict[board[y][x]] += 1

        word_dict = Counter(word)

        for c in word_dict:
            if c not in board_dict or board_dict[c] < word_dict[c]:
                return False

        # visit flag
        flags = [[0 for _ in range(n)] for _ in range(m)]

        def search(x, y, i) -> bool:
            # complete compare
            if i == word_len:
                return True

            # out of range
            if x >= n or x < 0 or y >= m or y < 0:
                return False
            
            # already visit
            if flags[y][x] == 1:
                return False

            # not equal word
            if board[y][x] != word[i]:
                return False

            flags[y][x] = 1
            direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

            for (x2, y2) in direction:
                if search(x + x2, y + y2, i + 1):
                    return True

            flags[y][x] = 0

            return False
        
        for y in range(m):
            for x in range(n):
                if search(x, y, 0):
                    return True

        return False