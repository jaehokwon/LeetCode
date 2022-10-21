class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack, result = [], 0

        for n in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[n]:
                stack.append(n)
        
        for n in range(len(nums) - 1, -1, -1):
            if not stack:
                break

            while stack and stack[-1] <= n and nums[stack[-1]] <= nums[n]:
                idx = stack.pop()
                result = max(result, n - idx)

        return result