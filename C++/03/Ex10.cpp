#include <iostream>
using namespace std;
int main() {
    string operation;
    double a, b;
    cout << "�����������������������\n";
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