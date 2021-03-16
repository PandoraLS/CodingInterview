/*
 * @Author: seenli
 * @Date: 2021-03-16 14:16:56
 * @LastEditors: seenli
 * @LastEditTime: 2021-03-16 15:49:06
 * @FilePath: \C++\131_PalindromePartitioning.cpp
 */

// ref: https://leetcode-cn.com/problems/palindrome-partitioning/solution/fen-ge-hui-wen-chuan-by-leetcode-solutio-6jkv/
// ������ ����+���仯����
// ���� ����+��̬�滮�ķ���������û��ʵ��

#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
private:
    vector<vector<int>> f;                              // f[i][j]��������Ƿ�������
    vector<vector<string>> ret;                         // ���շ��صĽ��
    vector<string> ans;                                 // ��ʱ�洢���ɻ��Ĵ�(��ʱ�ҵ�һ�ַָ��)
    int n;                                              // �����ַ�������

public:
    // ��s�еĵ�i�ʼ����
    void dfs(const string& s, int i) {
        if (i == n) {                                   // �ִ������ַ����һ��
            ret.push_back(ans);
            return;
        }
        for (int j = i; j < n; ++j) {                   // j��i��ʼ��Ӧ�����ַ������
            if (isPalindrome(s, i, j) == 1) {           // ���s�ǻ��Ĵ�
                ans.push_back(s.substr(i, j - i + 1));
                dfs(s, j + 1);                          // ���dfs�ҵ����������Ľ�����Ի�return�������в�����һ����
                ans.pop_back();                         // û���ҵ��ָ������֮ǰ�Ķ�����
            }
        }
    }

    // ���仯�����У�f[i][j] = 0 ��ʾδ������1 ��ʾ�ǻ��Ĵ���-1 ��ʾ���ǻ��Ĵ�
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