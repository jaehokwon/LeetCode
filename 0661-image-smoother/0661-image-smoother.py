class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        if len(img) <= 0 or len(img[0]) <= 0:
            return None
        
        m = len(img)
        n = len(img[0])

        def averageCell(x: int, y:int) -> int:
            count = 0
            summary = 0

            for j in range(y-1, y+2):
                if j < 0 or j >= m:
                    continue

                for i in range(x-1, x+2):
                    if i < 0 or i >= n:
                        continue

                    count = count + 1
                    summary = summary + img[j][i]

            return summary // count if count > 0 and summary > 0 else 0

        result = []

        for j in range(0, m):
            result.append([])
            for i in range(0, n):
                result[j].append(averageCell(i, j))
        
        return result