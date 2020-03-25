from collections import Counter, defaultdict


class Solution:
    """
    Sliding Window.
    """

    def minWindow1(self, s: str, t: str) -> str:
        """
        Use two pointers: left and right.
        Move right until window [left..right] contains all chars in t
        Then move left until window does not have all chars in t.
        Repeat 2 steps below to right reaches the end of s.
        """
        start, min_len = 0, float('inf')
        left, right = 0, 0

        needs = Counter(t)
        window = defaultdict(int)

        match = 0
        while right < len(s):
            # move right
            ch1 = s[right]
            window[ch1] += 1
            if window[ch1] == needs[ch1]:
                match += 1
            right += 1

            # move left
            while match == len(needs):
                # update min_len, start
                if right - left < min_len:
                    start = left
                    min_len = right - left
                ch2 = s[left]
                if ch2 in needs:
                    window[ch2] -= 1
                    if window[ch2] < needs[ch2]:
                        match -= 1
                left += 1

        return s[start:start + min_len] if min_len != float('inf') else ''

    def minWindow2(self, s: str, t: str) -> str:
        needs = Counter(t)
        missing = len(t)
        start, end = 0, float('inf')
        curr_start = 0

        for curr_end, ch in enumerate(s, 1):
            if needs[ch] > 0:
                missing -= 1
            needs[ch] -= 1

            if not missing:
                while needs[s[curr_start]] < 0:
                    needs[s[curr_start]] += 1
                    curr_start += 1
                if curr_end - curr_start < end - start:
                    start, end = curr_start, curr_end

                needs[s[curr_start]] += 1
                missing += 1
                curr_start += 1

        return s[start:end] if end != float('inf') else ''
