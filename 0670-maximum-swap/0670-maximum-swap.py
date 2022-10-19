class Solution:
    def maximumSwap(self, num: int) -> int:
        lst = list(str(num))
        n = len(lst)
        p, q, max_index = -1, -1, n - 1
        
        for i in range(max_index - 1, -1, -1):
            if lst[i] > lst[max_index]:
                max_index = i
            elif lst[i] < lst[max_index]:
                p, q = i, max_index
        
        lst[p], lst[q] = lst[q], lst[p]
        return int(''.join(lst))