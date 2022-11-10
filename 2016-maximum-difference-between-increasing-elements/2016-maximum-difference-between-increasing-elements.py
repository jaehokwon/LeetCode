class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_num, max_num, prev = nums[0], nums[0], nums[0]
        diff = -1
        
        for i in range(1, len(nums)):
            num = nums[i]
            if prev > num:
                max_num = num
            min_num = min(num, min_num)
            max_num = max(num, max_num)
            if min_num != max_num:
                diff = max(diff, max_num - min_num)
            prev = num
        
        return diff