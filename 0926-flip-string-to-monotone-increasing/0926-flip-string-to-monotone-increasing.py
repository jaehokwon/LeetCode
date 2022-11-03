class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        total = flip = 0

        for c in s:
            if c == '1':
                total += 1
            else:
                flip = min(flip + 1, total)

        return flip