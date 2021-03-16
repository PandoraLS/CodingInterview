/*
 * @Author: seenli
 * @Date: 2021-03-16 13:45:17
 * @LastEditors: seenli
 * @LastEditTime: 2021-03-16 14:04:32
 * @FilePath: \C++\String_125_ValidPalindrome.cpp
 */

// ref: https://leetcode-cn.com/problems/valid-palindrome/solution/yan-zheng-hui-wen-chuan-by-leetcode-solution/

#include <iostream>
#include <vector>
#include <string>
using namespace std;

// 双指针思路
class Solution {
public:
    bool isPalindrome(string s) {
        if (s == "") return true;
        string sgood;
        for (char ch: s) {
            if (isalnum(ch)) sgood += tolower(ch);
        }
        int n = sgood.size();
        int left = 0, right = n - 1;
        while(left < right) {
            if (sgood[left] != sgood[right]) {
                return false;
            }
            ++left;
            --right;
        }
        return true;
    }
};

int main() {
    // 手动输入字符串
    // string str1;
    // cin >> str1;
    string str1 = "A man, a plan, a canal: Panama";
    Solution s;
    auto res = s.isPalindrome(str1);
    cout << res << endl;;
    system("pause");
    return 0;
}