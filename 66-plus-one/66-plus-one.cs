public class Solution {
    public int[] PlusOne(int[] digits) {
        List<int> lst = new List<int>();

        for (int i=0; i<digits.Length; i++)
            lst.Add(digits[i]);

        for (int i=lst.Count - 1; i>=0; i--)
        {
            lst[i]++;

            if ((lst[i] %= 10) != 0)
                break;
                
            if (i == 0)
            {
                lst.Insert(0, 1);
                break;
            }
        }

        return lst.ToArray();
    }
}