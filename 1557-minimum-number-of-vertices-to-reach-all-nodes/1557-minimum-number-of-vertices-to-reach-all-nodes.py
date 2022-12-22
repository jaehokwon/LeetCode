class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        numbers = set([i for i in range(n)])
        for edge in edges:
            if edge[1] in numbers:
                numbers.remove(edge[1])
        return list(numbers)