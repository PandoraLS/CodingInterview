# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/3/10 9:25

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dfs_cnt(left, right, k):
            char_cnt = {}
            for i in range(left, right + 1):
                char_cnt[s[i]] = char_cnt.get(s[i], 0) + 1
            l, r = left, right
            # 先剔除掉右边的总数小于k的
            while l <= r and char_cnt[s[l]] < k:
                l += 1
            while l <= r and char_cnt[s[r]] < k:
                r -= 1
            if r - l + 1 < k: # 如果最后剩余的子串T的长度小于k，说明不存在这样的子串，返回0
                return 0

            p = l
            while p <= r and char_cnt[s[p]] >= k:
                p += 1
            if p > r:
                return r - l + 1
            return max(dfs_cnt(l, p - 1, k), dfs_cnt(p + 1, r, k)) # 此时s是被某个字符分割了

        return dfs_cnt(0, len(s) - 1, k)


if __name__ == '__main__':
    so = Solution()
    s = "ababbc"
    s2 = "abadbbc"
    print(so.longestSubstring(s2, 2))
