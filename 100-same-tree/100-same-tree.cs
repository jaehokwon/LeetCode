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
    public bool IsSameTree(TreeNode p, TreeNode q) {
        return CompareTree(p, q);
    }
    
    private bool CompareTree(TreeNode p, TreeNode q) {
        // 둘 다 null인 경우 다음을 비교할 필요가 없으므로 동일하다고 판단
        if (p == null && q == null)
            return true;
        
        // 둘의 값이 다를 경우 동일하지 않다고 판단
        if (p?.val != q?.val)
            return false;
        
        // 좌, 우 자식노드가 동일한지 여부 판단
        return CompareTree(p?.left, q?.left) && CompareTree(p?.right, q?.right);
    }
}