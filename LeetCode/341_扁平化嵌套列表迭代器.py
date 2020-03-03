# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.res = []
        self.dfs(nestedList)
        self.i = 0
        self.n = len(self.res)

    def dfs(self, v):
        if type(v) != list:
            self.res.append(v.getInteger())
        else:
            for _ in v:
                if _.isInteger():
                    self.res.append(_.getInteger())
                else:
                    self.dfs(_.getList())

    def next(self) -> int:
        ans = self.res[self.i]
        self.i += 1
        return ans

    def hasNext(self) -> bool:
        return self.i < self.n

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())