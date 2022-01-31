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
    public TreeNode ConvertBST(TreeNode root) {
        int currentValue = 0;
        
        if (root != null)
            dfs(root, currentValue);
        
        return root;
    }
    
    private int dfs(TreeNode root, int currentValue) {
        if (root.right != null)
            currentValue = dfs(root.right, currentValue);
        
        currentValue += root.val;
        root.val = currentValue;
        
        if (root.left != null)
            currentValue = dfs(root.left, currentValue);
        
        return currentValue;
    }
}