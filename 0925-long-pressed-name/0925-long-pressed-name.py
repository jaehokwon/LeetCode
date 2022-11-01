class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j, n, t = 0, 0, len(name), len(typed)

        while j < t:
            if i < n and name[i] == typed[j]:
                i += 1
            elif j == 0 or name[i - 1] != typed[j]:
                return False
            j += 1

        return i == n