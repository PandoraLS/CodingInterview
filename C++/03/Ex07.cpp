#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
void PrintF(string& StringPrint) {
    cout << StringPrint << ", ";
}
int main() {
    cout << "���������ַ�����" << endl;
    vector<string> studentName;
    vector<string>::iterator studentIterator;
    string str1, str2, str3;
    getline(cin, str1);
    getline(cin, str2);
    getline(cin, str3);
    studentName.push_back(str1);  //��vector��������Ϊ��vectorβ������һ������
    studentName.push_back(str2);
    studentName.push_back(str3);
    //���δ���������
    cout << "����ǰ���ַ���:" << endl;
    for_each(studentName.begin(), studentName.end(), PrintF);
    sort(studentName.begin(), studentName.end());  //������
    cout << "\n���������֣�" << endl;
    for_each(studentName.begin(), studentName.end(), PrintF);
    return 0;
}