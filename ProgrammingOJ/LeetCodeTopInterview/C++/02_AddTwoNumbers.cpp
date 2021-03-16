/*
 * @Author: seenli
 * @Date: 2021-03-11 00:10:42
 * @LastEditors: seenli
 * @LastEditTime: 2021-03-16 13:40:03
 * @FilePath: \C++\02_AddTwoNumbers.cpp
 * @Description: LeetCode Hot 100
 */

/*
    参考本地运行部分
    ref: https://leetcode-cn.com/problems/add-two-numbers/solution/cjie-ti-de-wan-zheng-dai-ma-bao-gua-sheng-cheng-ce/
*/

#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int len1 = 1; // 记录l1的长度
        int len2 = 1; // 记录l2的长度

        ListNode* p = l1;
        ListNode* q = l2;

        // 统计两ListNode的长度
        while(p->next != nullptr) {
            len1++;
            p = p->next;
        }
        while(q->next != nullptr) {
            len2++;
            q = q->next;
        }

        // 在短的链表末尾补零
        if (len1 > len2) {  // l2短
            for (int i = 1; i <= len1 - len2; i++) {
                q->next = new ListNode(0);
                q = q->next;
            }
        } else {       // l1短
            for (int i = 1; i <= len2 - len1; i++) {
                p->next = new ListNode(0);
                p = p->next;
            }
        }

        // 对齐相加考虑进位
        p = l1;
        q = l2;
        bool carry = false;                         // 记录进位
        ListNode* res = new ListNode(-1);           // 存放结果链表
        ListNode* r = res;                          // 指向结果链表的指针
        int sum = 0;                                // 记录两数加和
        while(p != nullptr && q != nullptr) {
            sum = carry + p->val + q->val;          // 记录两数求和+上一计算的进位
            r->next = new ListNode(sum % 10);       // 下一位的值(不含进位)
            carry = sum >= 10 ? true : false;       // 当前位计算是否有进位
            r = r->next;
            p = p->next;
            q = q->next;
        }
        if (carry) {                                // 如果还有进位则添加1到下一位
            r->next = new ListNode(1);
            r = r->next;
        }
        return res->next;                           // 返回结果列表
    }
};

ListNode* generateListNode(vector<int> vals);
void freeListNode(ListNode* head);
void printListNode(ListNode* head);

int main()
{
    auto list1 = generateListNode({2, 4, 3});
    auto list2 = generateListNode({5, 6, 4});
    printListNode(list1);
    printListNode(list2);
    Solution s;
    auto sum = s.addTwoNumbers(list1, list2);
    printListNode(sum);
    freeListNode(list1);
    freeListNode(list2);
    freeListNode(sum);
    system("pause");
    return 0;
}

// 生成list
ListNode* generateListNode(vector<int> vals) 
{
    ListNode *res = nullptr;
    ListNode *last = nullptr;                       // 确定是否走到list最后
    for(auto val : vals) {
        if(last) {
            last->next = new ListNode(val);
            last = last->next;
        }
        else {
            res = new ListNode(val);
            last = res;
        }
    }
    return res;
}

void printListNode(ListNode* head)
{
    ListNode* node = head;
    while(node) {
        cout << node->val << ", ";
        node = node->next;
    }
    cout << endl;
}

void freeListNode(ListNode* head)
{
    ListNode* node = head;
    while(node) {
        auto temp = node->next;
        delete node;
        node = temp;
    }
}
