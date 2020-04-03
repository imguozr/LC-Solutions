from collections import defaultdict
from typing import List


class Solution1:
    """
    Backtrack w/ dict
    """

    def __init__(self):
        self.words = []
        self.word_len = 0
        self.prefix_dict = {}

    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.words = words
        self.word_len = len(words[0])
        self.prefix_dict = self.build_prefix(self.words)

        res = []
        for word in self.words:
            square = [word]
            self.backtrack(1, square, res)
        return res

    def backtrack(self, step, square, res):
        if step == self.word_len:
            res.append(square[:])
            return

        prefix = ''.join([word[step] for word in square])
        for word in self.prefix_dict[prefix]:
            square.append(word)
            self.backtrack(step + 1, square, res)
            square.pop()

    def build_prefix(self, words):
        prefix_dict = defaultdict(set)
        for word in words:
            for prefix in (word[:i] for i in range(1, len(word))):
                prefix_dict[prefix].add(word)
        return prefix_dict


class Solution2:
    """
    Backtrack w/ Trie.
    """

    class TrieNode:

        def __init__(self):
            self.children = defaultdict(Solution2.TrieNode)
            self.is_word = False

    class Trie:

        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.root = Solution2.TrieNode()

        def insert(self, word: str) -> None:
            """
            Inserts a word into the trie.
            """
            curr = self.root
            for ch in word:
                curr = curr.children[ch]
            curr.is_word = True

        def search(self, word: str) -> bool:
            """
            Returns if the word is in the trie.
            """
            curr = self.root
            for ch in word:
                curr = curr.children.get(ch)
                if curr is None:
                    return False
            return curr.is_word

        def starts_with(self, prefix: str) -> bool:
            """
            Returns if there is any word in the trie that starts with the given prefix.
            """
            curr = self.root
            for ch in prefix:
                curr = curr.children.get(ch)
                if curr is None:
                    return False
            return True

        def words_start_with_prefix(self, prefix: str) -> List[str]:
            """
            Returns words start with prefix
            """
            if not self.starts_with(prefix):
                return []
            if self.search(prefix):
                return [prefix]

            curr = self.root
            for ch in prefix:
                curr = curr.children.get(ch)
            return self._get_word(prefix, curr)

        def _get_word(self, prefix, node):
            if not node:
                return []

            word_list = []
            if node.is_word:
                word_list.append(prefix)
            for key in node.children.keys():
                word_list += self._get_word(prefix + key, node.children.get(key))
            return word_list

    def __init__(self):
        self.words = []
        self.word_len = 0
        self.trie = Solution2.Trie()

    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.words = words
        self.word_len = len(words[0])
        self.trie = self.build_trie(self.words)

        res = []
        for word in self.words:
            square = [word]
            self.backtrack(1, square, res)
        return res

    def backtrack(self, step, square, res):
        if step == self.word_len:
            res.append(square[:])
            return

        prefix = ''.join([word[step] for word in square])
        word_list = self.trie.words_start_with_prefix(prefix)
        for word in word_list:
            square.append(word)
            self.backtrack(step + 1, square, res)
            square.pop()

    def build_trie(self, words):
        tree = Solution2.Trie()
        for word in words:
            tree.insert(word)
        return tree
