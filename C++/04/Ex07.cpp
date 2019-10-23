#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    char operation;
    double a = 0.0, b = 0.0;
    string str_a, str_b;
    double str_a_num, str_b_num;
    vector<string> vs = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    vector<int> vi    = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    cout << "输入两操作数与操作符\n";
    do {
        cout << "输入数字形式的数据 a b operation: \n";
        cin >> a >> b >> operation;
        if (operation == '+') {
            cout << "The sum of " << a << " and " << b << " is " << a + b << " \n";
        } else if (operation == '-') {
            cout << "The difference of " << a << " and " << b << " is " << a - b << " \n";
        } else if (operation == '*') {
            cout << "The product of " << a << " and " << b << " is " << a * b << " \n";
        } else if (operation == '/') {
            cout << "The quotient of " << a << " and " << b << " is " << a / b << " \n";
        } else if (operation == '%') {
            cout << "The mod of " << a << " and " << b << " is " << int(a) % int(b) << " \n";
        } else {
            cout << "未知运算！\n";
        }

        cout << "输入拼写形式的数据 str_a str_b operation: \n";
        cin >> str_a >> str_b >> operation;
        for (int i = 0; i < 10; i++) {
            if (str_a == vs[i]) {
                str_a_num = vi[i];
                break;  //找到对应的数后，就退出当前for循环
            } else {
                str_a_num = -1;
            }
        }
        for (int i = 0; i < 10; i++) {
            if (str_b == vs[i]) {
                str_b_num = vi[i];
                break;  //找到对应的数后，就退出当前for循环
            } else {
                str_b_num = -1;
            }
        }
        if (operation == '+') {
            cout << "The sum of " << str_a << " and " << str_b << " is " << str_a_num + str_b_num << " \n";
        } else if (operation == '-') {
            cout << "The difference of " << str_a << " and " << str_b << " is " << str_a_num - str_b_num << " \n";
        } else if (operation == '*') {
            cout << "The product of " << str_a << " and " << str_b << " is " << str_a_num * str_b_num << " \n";
        } else if (operation == '/') {
            cout << "The quotient of " << str_a << " and " << str_b << " is " << str_a_num / str_b_num << " \n";
        } else if (operation == '%') {
            cout << "The mod of " << str_a << " and " << str_b << " is " << int(str_a_num) % int(str_b_num) << " \n";
        } else {
            cout << "未知运算！\n";
        }
        cout << " \n";
    } while (true);
    return 0;
}
