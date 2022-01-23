public class Solution {
    public int[] FindRightInterval(int[][] intervals) {
        int[] res = new int[intervals.Length];

        for (int i=0; i<intervals.Length; i++)
        {
            int targetIndex = -1;
            int startj = int.MaxValue;

            for (int j=0; j<intervals.Length; j++)
            {
                if (intervals[j][0] < intervals[i][1])
                    continue;

                if (startj > intervals[j][0])
                {
                    targetIndex = j;
                    startj = intervals[j][0];
                }
            }

            res[i] = targetIndex;
        }

        return res;
    }
}