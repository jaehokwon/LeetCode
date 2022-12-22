class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        count = 0
        for i, v in enumerate(height):
            while stack and height[stack[-1]] < v:
                mid = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                right = i
                count += (min(height[left], height[right]) -
                          height[mid]) * (right - left - 1)
            stack.append(i)
        return count