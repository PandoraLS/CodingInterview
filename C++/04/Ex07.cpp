#include <iostream>
using namespace std;
int main(void) {
    char operation;
    double a = 0.0, b = 0.0;
    string str_a, str_b;
    cout << "�������������������\n";
    // TODO 
    do {
        cout << "����������ʽ������ a b operation: \n";
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
            cout << "δ֪���㣡\n";
        }

        cout << "����ƴд��ʽ������ a b operation: \n";
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
            cout << "δ֪���㣡\n";
        }
    } while (true);
    return 0;
}
