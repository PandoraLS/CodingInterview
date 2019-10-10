#include <iostream>
using namespace std;
int main() {
    string operation;
    double a, b;
    cout << "输入操作符和两个操作数：\n";
    while (cin >> operation >> a >> b) {
        cout << operation << "    " << a << "   " << b << "\nresult:  ";
        if (operation == "+") {
            cout << a + b << "\n";
        } else if (operation == "-") {
            cout << a - b << "\n";
        } else if (operation == "*") {
            cout << a * b << "\n";
        } else if (operation == "/") {
            cout << a / b << "\n";
        } else {
            cout << "Error!\n";
        }
    }
    return 0;
}