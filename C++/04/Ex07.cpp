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
    cout << "�������������������\n";
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

        cout << "����ƴд��ʽ������ str_a str_b operation: \n";
        cin >> str_a >> str_b >> operation;
        for (int i = 0; i < 10; i++) {
            if (str_a == vs[i]) {
                str_a_num = vi[i];
                break;  //�ҵ���Ӧ�����󣬾��˳���ǰforѭ��
            } else {
                str_a_num = -1;
            }
        }
        for (int i = 0; i < 10; i++) {
            if (str_b == vs[i]) {
                str_b_num = vi[i];
                break;  //�ҵ���Ӧ�����󣬾��˳���ǰforѭ��
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
            cout << "δ֪���㣡\n";
        }
        cout << " \n";
    } while (true);
    return 0;
}
