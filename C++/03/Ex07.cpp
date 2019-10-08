#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
void PrintF(string& StringPrint) {
    cout << StringPrint << ", ";
}
int main() {
    cout << "输入三个字符串：" << endl;
    vector<string> studentName;
    vector<string>::iterator studentIterator;
    string str1, str2, str3;
    getline(cin, str1);
    getline(cin, str2);
    getline(cin, str3);
    studentName.push_back(str1);  //在vector类中作用为在vector尾部加入一个数据
    studentName.push_back(str2);
    studentName.push_back(str3);
    //输出未排序的名字
    cout << "排序前的字符串:" << endl;
    for_each(studentName.begin(), studentName.end(), PrintF);
    sort(studentName.begin(), studentName.end());  //排序函数
    cout << "\n排序后的名字：" << endl;
    for_each(studentName.begin(), studentName.end(), PrintF);
    return 0;
}