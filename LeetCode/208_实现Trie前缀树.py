# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/22 12:34

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = set()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.words.add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        for word in self.words:
            if word.startswith(prefix):
                return True
        return False


class Trie2:
    # 字典树
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.trie
        for c in word:
            node = node.setdefault(c, {})
        node['#'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.trie
        for c in word:
            if c not in node:
                return False
            node = node[c]
        if '#' in node:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.trie
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True


class Node:
    def __init__(self):
        self.next = {}
        self.is_word = False


class Trie3:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self._insert(self.root, word, 0)

    def _insert(self, node, word, d):
        if d == len(word):
            node.is_word = True
            return node
        c = word[d]
        if c not in node.next:
            node.next[c] = Node()
        node.next[c] = self._insert(node.next[c], word, d + 1)
        return node

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        x = self._search(self.root, word, 0)
        if x is None:
            return False
        return x.is_word is True

    def _search(self, node, word, d):
        if d == len(word):
            return node
        c = word[d]
        if c not in node.next:
            return None
        return self._search(node.next[c], word, d + 1)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        x = self._search(self.root, prefix, 0)
        if x is None:
            return False
        return True


if __name__ == '__main__':
    from pprint import pprint
    obj = Trie2()
    obj.insert("apple")
    print(obj.search("apple"))  # 返回True
    print(obj.search("app"))  # 返回False
    print(obj.startsWith("app"))  # 返回True
    obj.insert("app")  # 返回False
    print(obj.search("app"))  # 返回False
    obj.insert("eat")
    obj.insert("eval")
    obj.insert("appreciate")
    obj.insert("abc")
    obj.insert("access")
    pprint(obj.trie)
    
    
