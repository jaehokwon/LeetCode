class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        def averageCell(img: List[List[int]], x: int, y:int) -> int:
            if len(img) <= 0 or len(img[0]) <= 0:
                return 0

            count = 0
            summary = 0

            for i in range(x-1, x+2):
                if i < 0 or i >= len(img[0]):
                    continue

                for j in range(y-1, y+2):
                    if j < 0 or j >= len(img):
                        continue

                    count = count + 1
                    summary = summary + img[j][i]

            return math.floor(summary/count) if count > 0 and summary > 0 else 0

        if len(img) <= 0 or len(img[0]) <= 0:
            return None
        
        result = []

        for j in range(0, len(img)):
            result.append([])
            for i in range(0, len(img[j])):
                result[j].append(averageCell(img, i, j))
        
        return result

