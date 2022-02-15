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

        // tuple<현재 노드의 level, 노드>을 담을 queue 생성
        Queue<(int lv, TreeNode node)> queue = new Queue<(int lv, TreeNode node)>();
        queue.Enqueue((0, root));
        int lv = 0;
        int sum = 0;

        while (queue.Count != 0)
        {
            var tp = queue.Dequeue();

            // 이전 level과 현재 level이 다를 경우 sum 값 초기화
            if (tp.lv != lv)
                sum = tp.node.val;
            else
                sum += tp.node.val;
            
            lv = tp.lv;

            // 하위 노드를 담을 때 현재 노드의 level + 1하여 queue에 삽입 후 층별 순회
            if (tp.node.left != null)
                queue.Enqueue((tp.Item1 + 1, tp.node.left));

            if (tp.node.right != null)
                queue.Enqueue((tp.Item1 + 1, tp.node.right));
        }

        return sum;
    }
}