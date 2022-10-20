class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        word_len = len(word)

        # 방문 여부 flag
        flags = [[0 for _ in range(n)] for _ in range(m)]

        def search(x, y, i) -> bool:
            # 전체 단어 비교 완료 시
            if i == word_len:
                return True

            # out of range
            if x >= n or x < 0 or y >= m or y < 0:
                return False
            
            # alreay visit
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