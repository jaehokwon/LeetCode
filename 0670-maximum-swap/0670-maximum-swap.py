class Solution:
    def maximumSwap(self, num: int) -> int:
        res = [char for char in str(num)]
        lst_copy = copy.deepcopy(res)
        count = len(res)
        max_num = num
        
        for i in range(0, count - 1):
            for j in range(i + 1, count):
                if res[i] < res[j]:
                    lst_copy[i], lst_copy[j] = lst_copy[j], lst_copy[i]
                    
                    if max_num < int(''.join(lst_copy)):
                        max_num = int(''.join(lst_copy))
                        
                    lst_copy[i], lst_copy[j] = lst_copy[j], lst_copy[i]
            
            if num < max_num:
                break
        
        return max_num
    