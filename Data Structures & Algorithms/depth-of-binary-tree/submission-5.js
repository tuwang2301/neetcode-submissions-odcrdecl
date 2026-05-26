/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    maxDepth(root) {
        let depth = 0

        function dfs(root, depth){
            if (!root){
                return depth
            }
            let left = dfs(root.left, depth + 1)
            let right = dfs(root.right, depth + 1)
            return Math.max(left, right)
        }

        return dfs(root, depth)
    }
}
