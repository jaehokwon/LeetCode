/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public int DeepestLeavesSum(TreeNode root)
    {
        if (root == null)
            return 0;

        Queue<(int, TreeNode)> queue = new Queue<(int, TreeNode)>();
        queue.Enqueue((0, root));
        int lv = 0;
        int sum = 0;

        while (queue.Count != 0)
        {
            var tp = queue.Dequeue();

            if (tp.Item1 != lv)
                sum = tp.Item2.val;
            else
                sum += tp.Item2.val;

            lv = tp.Item1;
            if (tp.Item2.left != null)
                queue.Enqueue((tp.Item1 + 1, tp.Item2.left));

            if (tp.Item2.right != null)
                queue.Enqueue((tp.Item1 + 1, tp.Item2.right));
        }

        return sum;
    }
}