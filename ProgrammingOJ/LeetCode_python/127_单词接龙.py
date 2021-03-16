# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/16 9:56

from collections import defaultdict
from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        path_len = {beginWord: 1}
        q = deque([beginWord])
        while q:
            word = q.popleft()
            for i in range(len(word)):
                newword = list(word)
                for c in list(map(chr, range(ord('a'), ord('z') + 1))):
                    newword[i] = c
                    str_newword = ''.join(newword)
                    if str_newword in word_set and str_newword == endWord:
                        return path_len[word] + 1
                    if str_newword in word_set and str_newword not in path_len:
                        q.append(str_newword)
                        path_len[str_newword] = path_len[word] + 1
        return 0


class Solution2(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # 所有的单词长度是一样的，均为L
        L = len(beginWord)

        # 字典用于保存可以形成的单词的组合
        # 对任一给定单词word，每次更替一个字母
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # 键是通用状态
                # 值是所有具有通用状态的单词
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        # Queue for BFS
        queue = [(beginWord, 1)]
        # Visited to make sure we don't repeat processing same word.防止有环出现
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)
            for i in range(L):
                # 当前单词的中间词
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]

                # Next states are all the words which share the same intermediate state.
                # 下一个状态是所有处于相同中间状态的单词。
                for word in all_combo_dict[intermediate_word]:
                    # 我们是否找到了我们想要的，也就是endword
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    so = Solution()
    print(so.ladderLength(beginWord=beginWord, endWord=endWord, wordList=wordList))
