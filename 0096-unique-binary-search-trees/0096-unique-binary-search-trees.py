class Solution:
    def numTrees(self, n: int) -> int:
        cache = [0] * (n+1)
        cache[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                cache[i] += cache[j] * cache[i-j-1]
        return cache[n]