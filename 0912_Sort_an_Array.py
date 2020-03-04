import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)

    # TLE
    def bubble_sort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    # TLE
    def insert_sort_1(self, nums):
        n = len(nums)
        if n == 1:
            return nums
        for i in range(1, n):
            for j in range(i, 0, -1):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                else:
                    break
        return nums

    # TLE
    def insert_sort_2(self, nums):
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return nums

    # TLE
    # O(N^2)
    def selection_sort(self, nums):
        for i in range(len(nums)):
            _min = min(nums[i:])
            min_index = nums[i:].index(_min)
            nums[i + min_index] = nums[i]
            nums[i] = _min
        return nums

    def quick_sort_1(self, nums):
        if len(nums) <= 1:
            return nums

        pivot = random.choice(nums)
        ls = [n for n in nums if n < pivot]
        eq = [n for n in nums if n == pivot]
        gr = [n for n in nums if n > pivot]
        return self.quick_sort_1(ls) + eq + self.quick_sort_1(gr)

    def quick_sort_2(self, nums):
        def helper(head, tail):
            if head >= tail:
                return
            l, r = head, tail
            mid = (l + r) // 2
            pivot = nums[mid]
            while r >= l:
                while r >= l and nums[l] < pivot:
                    l += 1
                while r >= l and nums[r] > pivot:
                    r -= 1
                if r >= l:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            helper(head, r)
            helper(l, tail)

        helper(0, len(nums) - 1)
        return nums

    def merge_sort(self, nums):
        def merge(left, right):
            res = []
            while left and right:
                if left[0] <= right[0]:
                    res.append(left.pop(0))
                else:
                    res.append(right.pop(0))
            if left:
                res += left
            if right:
                res += right
            return res

        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return merge(left, right)

    def heap_sort(self, nums):
        def heapify(start, end):
            root = start
            while True:
                child = 2 * root + 1
                if child > end:
                    break
                if child + 1 <= end and nums[child] < nums[child + 1]:
                    child += 1
                if nums[root] < nums[child]:
                    nums[root], nums[child] = nums[child], nums[root]
                    root = child
                else:
                    break

        n = len(nums)
        for s in range((n - 2) // 2, -1, -1):
            heapify(s, n - 1)

        for e in range(n - 1, 0, -1):
            nums[0], nums[e] = nums[e], nums[0]
            heapify(0, e - 1)

        return nums
