class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for word in words:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        res = sorted(dic, key=lambda x: (-dic[x], x))
        return res[:k]