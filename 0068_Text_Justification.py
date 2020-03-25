from typing import List


class Solution:
    """
    Very Straightforward.
    """
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        res, curr, curr_width = [], [], 0
        for word in words:
            if len(curr) + len(word) + curr_width > max_width:
                if len(curr) == 1:
                    curr_str = curr[0] + (' ' * (max_width - curr_width))
                else:
                    curr_str = self.generate(curr, curr_width, max_width)
                res.append(curr_str)
                curr, curr_width = [], 0
            curr.append(word)
            curr_width += len(word)
        return res + [' '.join(curr).ljust(max_width)]

    def generate(self, curr, curr_width, max_width):
        res = ''
        count = len(curr)
        total_space = max_width - curr_width
        average, more = divmod(total_space, count - 1)
        i = 0
        for word in curr:
            res += word + (' ' * average)
            if i < more:
                res += ' '
                i += 1
        return res.rstrip()
