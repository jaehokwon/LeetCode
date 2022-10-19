class Solution:
    def maximumSwap(self, num: int) -> int:
        res = [char for char in str(num)]
        count = len(res)
        max_num = num
        
        for i in range(0, count - 1):
            for j in range(i + 1, count):
                if res[i] < res[j]:
                    res[i], res[j] = res[j], res[i]
                    current_num = int(''.join(res))
                    
                    if max_num < current_num:
                        max_num = current_num
                        
                    res[i], res[j] = res[j], res[i]
            
            if num < max_num:
                break
        
        return max_num
    