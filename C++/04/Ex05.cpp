#include <iostream>
using namespace std;
int main(void) {
    char operation;
    double a = 0.0, b = 0.0;
    cout << "输入两操作数与操作符\n";
    while (cin >> a >> b >> operation) {
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
    }
    return 0;
}
