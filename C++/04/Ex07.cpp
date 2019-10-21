#include <iostream>
using namespace std;
int main(void) {
    char operation;
    double a = 0.0, b = 0.0;
    string str_a, str_b;
    cout << "输入两操作数与操作符\n";
    // TODO 
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

        cout << "输入拼写形式的数据 a b operation: \n";
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
    } while (true);
    return 0;
}
