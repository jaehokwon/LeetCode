class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        cnt = len(nums)
        dic = {}
        for lst in nums:
            for num in lst:
                if num in dic:
                    dic[num] += 1
                else:
                    dic[num] = 1
                
        return sorted([k for k,v in dic.items() if v == cnt])