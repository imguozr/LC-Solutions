from collections import defaultdict, deque
from typing import List


class Solution:
    """
    BFS
    Use dict to store adjacent nodes
    """

    def ladderLength(self, begin: str, end: str, words: List[str]) -> int:
        if not begin or not end or not words or end not in words:
            return 0

        # word length
        l = len(begin)
        # a map of all combinations of words with missing letters
        # mapped to all words in the list that match that pattern.
        # E.g. hot -> {'*ot': ['hot'], 'h*t': ['hot'], 'ho*': ['hot']}
        dic = defaultdict(list)
        for word in words:
            for i in range(l):
                dic[word[:i] + '*' + word[i + 1:]].append(word)

        # BFS Template
        queue = deque([(begin, 1)])
        seen = {begin}

        while queue:
            word, depth = queue.popleft()
            for i in range(l):
                tmp = word[:i] + '*' + word[i + 1:]
                for neighbor in dic[tmp]:
                    if neighbor == end:
                        return depth + 1
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, depth + 1))
                        
        return 0
