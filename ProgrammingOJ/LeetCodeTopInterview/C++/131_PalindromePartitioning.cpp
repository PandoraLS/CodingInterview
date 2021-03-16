/*
 * @Author: seenli
 * @Date: 2021-03-16 14:16:56
 * @LastEditors: seenli
 * @LastEditTime: 2021-03-16 15:49:06
 * @FilePath: \C++\131_PalindromePartitioning.cpp
 */

// ref: https://leetcode-cn.com/problems/palindrome-partitioning/solution/fen-ge-hui-wen-chuan-by-leetcode-solutio-6jkv/
// 方法： 回溯+记忆化搜索
// 还有 回溯+动态规划的方法，这里没有实现

#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
private:
    vector<vector<int>> f;                              // f[i][j]用来标记是否被搜索过
    vector<vector<string>> ret;                         // 最终返回的结果
    vector<string> ans;                                 // 临时存储若干回文串(此时找到一种分割方案)
    int n;                                              // 输入字符串长度

public:
    // 从s中的第i项开始搜索
    void dfs(const string& s, int i) {
        if (i == n) {                                   // 抵达输入字符最后一个
            ret.push_back(ans);
            return;
        }
        for (int j = i; j < n; ++j) {                   // j从i开始对应单个字符的情况
            if (isPalindrome(s, i, j) == 1) {           // 如果s是回文串
                ans.push_back(s.substr(i, j - i + 1));
                dfs(s, j + 1);                          // 如果dfs找到满足条件的结果，自会return，就运行不到下一行了
                ans.pop_back();                         // 没有找到分割方案，则之前的都回溯
            }
        }
    }

    // 记忆化搜索中，f[i][j] = 0 表示未搜索，1 表示是回文串，-1 表示不是回文串
    int isPalindrome(const string& s, int i, int j) {
        if (f[i][j]) {
            return f[i][j];
        }
        if (i >= j) {
            return f[i][j] = 1;
        }
        return f[i][j] = (s[i] == s[j] ? isPalindrome(s, i + 1, j - 1): -1);
    }
    

    vector<vector<string>> partition(string s) {
        n = s.size();
        f.assign(n, vector<int>(n));

        dfs(s, 0);
        return ret;
    }
};

int main() {
    string str1 = "aab";
    Solution s;
    auto res = s.partition(str1);
    for (auto vec_str: res) {
        for (auto str: vec_str) {
            cout << str << ' ';
        }
        cout << endl;
    }
    system("pause");
    return 0;
}