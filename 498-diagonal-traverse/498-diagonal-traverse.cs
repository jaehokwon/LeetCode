public class Solution {
    public int[] FindDiagonalOrder(int[][] mat) {
        List<int> res = new List<int>();

        SetLocation(mat, res, (0, 0), true);

        return res.ToArray();
    }

    void SetLocation(int[][] mat, List<int> res, (int x, int y) loc, bool up)
    {
        res.Add(mat[loc.y][loc.x]);

        if (loc.y == mat.Length - 1 && loc.x == mat[0].Length - 1)
            return;

        (int x, int y) locChange = (loc.x + (up ? 1 : -1), loc.y + (up ? -1 : 1));

        bool valid = true;

        if (locChange.x < 0 || locChange.y < 0 || locChange.x > mat[0].Length - 1 || locChange.y > mat.Length - 1)
            valid = false;

        if (!valid)
        {
            if (up){
                if (loc.x + 1 <= mat[0].Length - 1)
                    loc.x++;
                else
                    loc.y++;
            }
            else{
                if (loc.y + 1 <= mat.Length - 1)
                    loc.y++;
                else
                    loc.x++;
            }

            locChange = loc;
            up = !up;
        }

        SetLocation(mat, res, locChange, up);
    }
}