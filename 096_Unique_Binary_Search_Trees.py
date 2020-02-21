class Solution:
    """
        Consider to generate a BST with root i.
        The left subtree of the BST should have values
            in the sub-sequence of [1 ... i - 1] and have i - 1 nodes.
        The right subtree of the BST should have values
            in the sub-sequence of [i + 1 ... n] and have n - i nodes.
        We can recursively generate subtrees using such sub-sequences.
        With this method, all BSTs we have must be unique since they have unique roots.
        So, the # of BSTs (G) = sum(# of BSTs with root i, i in [1 ... n])
        And # of BSTs with root i (F) = # of left subtrees * # of right subtrees.
        =>  F(i, n) = G(i - 1) * G(n - i)
    """

    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                # F(j, i) = G(j - 1) * G(i - j)
                # j is root of BST, i is biggest number.
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
