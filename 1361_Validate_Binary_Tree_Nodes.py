class Solution:
    """
        DFS and HashSet.
    """

    def validateBinaryTreeNodes(self, n: int, left: list[int], right: list[int]) -> bool:
        stack = [0]
        visited = {0}
        while stack:
            node = stack.pop(0)
            l, r = left[node], right[node]
            if l == -1 and r == -1:
                continue
            if l != -1:
                if l in visited:
                    return False
                visited.add(l)
                stack.append(l)
            if r != -1:
                if r in visited:
                    return False
                visited.add(r)
                stack.append(r)

        return len(visited) == n
