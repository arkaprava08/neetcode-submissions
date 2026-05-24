/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int max=Integer.MIN_VALUE;
    public int maxMan(TreeNode root) {
        if(root == null) {
            return 0;
        }
        

        int maxLeft = maxMan(root.left);
        int maxRight = maxMan(root.right);
System.out.println("ARKA: " + root.val + " : " + maxLeft + " : " + maxRight);
System.out.println(max);
        max = Math.max(max, root.val);
System.out.println(max);
        max = Math.max(max, (maxLeft + maxRight + root.val));
System.out.println(max);
        if(root.left != null)
            max = Math.max(max, maxLeft + root.val);
System.out.println(max);
        if(root.right != null)
            max = Math.max(max, maxRight + root.val);
System.out.println(max);

        return Math.max(Math.max(root.val, root.val+maxLeft), root.val+maxRight);
    }
    public int maxPathSum(TreeNode root) {
        maxMan(root);
        return max;
    }
}
