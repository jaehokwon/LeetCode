class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a == 1:
            return 1
        num = 0
        len_b = len(b)
        for i, v in enumerate(b):
            num += pow(10, len_b-i-1) * v
        return pow(a, num, 1337)