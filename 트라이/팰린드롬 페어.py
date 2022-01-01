#336

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict()
        self.word_id = -1
        self.palindrome_word_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def is_palindrome(word):
        return word[::] == word[::-1]

    def insert(index, word):
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index