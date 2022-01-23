public class Solution {
    public int ThirdMax(int[] nums) {
        Array.Sort(nums);
        int num = int.MaxValue;
        int interval = 0;

        for (int i=nums.Length - 1; i>=0; i--)
        {
            if (nums[i] < num)
            {
                num = nums[i];

                if (++interval >= 3)
                    break;
            }
        }

        return interval >= 3 ? num : nums[nums.Length - 1];
    }
}