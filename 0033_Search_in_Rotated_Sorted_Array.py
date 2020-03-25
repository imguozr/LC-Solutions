from typing import List


class Solution:
    """
    Binary Search.
    """

    def search1(self, nums: List[int], target: int) -> int:
        """
        Two passes. Find pivot first, then search in each half.
        """

        def find_pivot():
            """
            Find pivot, which is the largest # in the list.
            """
            left, right = 0, len(nums) - 1
            if nums[left] < nums[right]:
                return right
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    if nums[mid] < nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1

        def search(left, right):
            """
            search for target in specific half.
            """
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                else:
                    if nums[mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
            return -1

        n = len(nums)
        if not n:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1

        pivot = find_pivot()
        if nums[pivot] == target:
            return pivot
        if pivot == n - 1:
            return search(0, n - 1)
        if target < nums[0]:
            return search(pivot + 1, n - 1)
        return search(0, pivot - 1)

    def search2(self, nums: List[int], target: int) -> int:
        """
        One pass.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    # target in the non-rotated list
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                if nums[mid] < target <= nums[right]:
                    # target in the non-rotated list
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
