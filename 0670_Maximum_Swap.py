class Solution:
    """
        Intuition: At each digit of the input number in order,
        if there is a larger digit that occurs later,
        we know that the best swap must occur with that exact digit.

        Algo: when scanning the number from left to right,
        if there is a larger digit in the future,
        we will swap it with the largest such digit;
        if there are multiple such digits,
        we will swap it with the one that occurs the latest.
    """

    def maximumSwap(self, num: int) -> int:
        nums = list(map(int, str(num)))
        # Store last index of digits.
        last = {v: i for i, v in enumerate(nums)}
        for i, v in enumerate(nums):
            for d in range(9, v, -1):
                if last.get(d):
                    tmp = last[d]
                    if tmp > i:
                        nums[i], nums[tmp] = nums[tmp], nums[i]
                        return int(''.join(map(str, nums)))
        return num
