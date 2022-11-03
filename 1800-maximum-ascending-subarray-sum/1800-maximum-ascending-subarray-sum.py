class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        prev = sum = 0
        max_num = 0

        for i in nums:
            if prev >= i:
                max_num = max(max_num, sum)
                sum = 0
            
            sum += i
            prev = i
        
        max_num = max(max_num, sum)

        return max_num