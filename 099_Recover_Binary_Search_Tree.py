class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
        Firstly, we should notice that the in-order of BST will be a sorted list.
        If two nodes are swapped in mistake, the in-order list will be have 1~2 downs.
        (The former > the latter)

        So, we can traverse the BST in-orderly, find two swapped nodes and then recover it, that's Solution 1.
        Also, when traversing the BST, we can find these two nodes at the same time. Then recover the tree.
        Traverse the BST iteratively, recursively and using Morris algorithm contribute to Solution 2-4 respectively.
    """

    def recoverTree_1(self, root: TreeNode) -> None:
        """
            Time complexity: O(n)
            [In-order traverse: O(n), Find swap and recover: Best case O(1), Worst case O(n)].
            Space complexity: O(n).
        """

        def in_order(r):
            return in_order(r.left) + [r.val] + in_order(r.right) if r else []

        def find_swap(nums):
            """
                Traversing the in-order list to find peeks.
                >> 1234 -> 1324
                We have 1 down: 32.
                >> 12345 -> 14325
                We have 2 downs: 43 and 32.

                To find the swapped number, we can declare x and y to record peeks.
                x is the former one and y is the latter one.
                If x is defined, we know that the former mistake is found.
                And y will be re-defined, aiming to capture the latter mistake.
            """
            n = len(nums)
            x = y = -1
            for i in range(n - 1):
                if nums[i] > nums[i + 1]:
                    y = nums[i + 1]
                    if x == -1:
                        x = nums[i]
                    else:
                        break
            return x, y

        def recover(r, count=2):
            if r:
                if r.val == x or r.val == y:
                    r.val = y if r.val == x else x
                    count -= 1
                    if not count:
                        return
                recover(r.left, count)
                recover(r.right, count)

        tree = in_order(root)
        x, y = find_swap(tree)
        recover(root, 2)

    def recoverTree_2(self, root: TreeNode) -> None:
        """
            Time complexity: Best case O(1), Worst case O(n) (On eof the nodes is right-most)
            Space complexity: O(h).
        """
        stack = []
        x = y = pre = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            # Below this: What to do.
            # Find wrong nodes in one pass.
            if pre and root.val < pre.val:
                y = root
                if x is None:
                    x = pre
                else:
                    break
            pre = root
            # Above this: What to do.

            root = root.right

        x.val, y.val = y.val, x.val

    def recoverTree_3(self, root: TreeNode) -> None:
        """
            Time complexity: Best case O(1), Worst case O(n)
            Space complexity: O(h).
        """

        def find_swap(r):
            nonlocal x, y, pre
            if r is None:
                return

            find_swap(r.left)

            # Below this: What to do.
            # Find wrong nodes in one pass.
            if pre and r.val < pre.val:
                y = r
                if x is None:
                    x = pre
                else:
                    return
            pre = r
            # Above this: What to do.

            find_swap(r.right)

        x = y = pre = None
        find_swap(root)
        x.val, y.val = y.val, x.val

    def recoverTree_4(self, root: TreeNode) -> None:
        """
            Time complexity: O(n).
            Space complexity: O(1).
        """
        x = y = pre = None

        while root:
            # If there is a left child then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it. (Do something.)
            if root.left:
                # Predecessor node is one step left and then right till you can.
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right

                # set link predecessor.right = root
                # go to explore left subtree
                if predecessor.right is None:
                    predecessor.right = root
                    root = root.left
                else:
                    # Below this: What to do.
                    # Find wrong nodes in one pass.
                    if pre and root.val < pre.val:
                        y = root
                        if x is None:
                            x = pre
                    pre = root
                    # Above this: What to do.

                    # break link predecessor.right = root
                    # change subtree and go right
                    predecessor.right = None
                    root = root.right

            # If there is no left child, just go right.
            else:
                # Below this: What to do.
                # Find wrong nodes in one pass.
                if pre and root.val < pre.val:
                    y = root
                    if x is None:
                        x = pre
                pre = root
                # Above this: What to do.

                root = root.right

        x.val, y.val = y.val, x.val
