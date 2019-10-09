#include <iostream>
using namespace std;
int main() {
    int number = 0;
    cout << "判断奇偶数,请输入一个int数字\n";
    cin >> number;
    cout << "通过按位与的方式判断奇偶: ";
    if (number & 1) { // 通过按位与的方式判断奇偶
        cout << "The value " << number << " is an odd number\n";
    } else {
        cout << "The value " << number << " is an even number\n";
    }

    cout << "通过取余的方式判断奇偶: ";
    if (number % 2) { // 通过取余的方式判断奇偶
        cout << "The value " << number << " is an odd number\n";
    } else {
        cout << "The value " << number << " is an even number\n";
    }
    return 0;
}