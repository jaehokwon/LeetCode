class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dic = defaultdict(int)

        def dfs(index=0, sum=0):
            key = (index, sum)
            if key not in dic:
                if len(nums) == index:
                    return 1 if target == sum else 0
                else:
                    dic[key] = dfs(index + 1, sum + nums[index]) + \
                        dfs(index + 1, sum - nums[index])
            return dic[key]
        return dfs()