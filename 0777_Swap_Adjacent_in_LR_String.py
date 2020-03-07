class Solution:
    """
        Intuition:
            1. L will always move to the left, R will always move to the right
            2. L & R will not cross over each other.

        Algorithm:
            1. L, R will remain in same relative location.
            2. L index in start will bigger than idx in end.
            3. R index in start will smaller than idx in start.
    """

    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False

        A = [(s, idx) for idx, s in enumerate(start) if s in ('L', 'R')]
        B = [(s, idx) for idx, s in enumerate(end) if s in ('L', 'R')]

        if len(A) != len(B):
            return False

        for (s, i), (e, j) in zip(A, B):
            if s != e:
                return False
            if s == 'L':
                if i < j:
                    return False
            if s == 'R':
                if i > j:
                    return False

        return True
