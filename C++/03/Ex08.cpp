#include <iostream>
using namespace std;
int main() {
    int number = 0;
    cout << "�ж���ż��,������һ��int����\n";
    cin >> number;
    cout << "ͨ����λ��ķ�ʽ�ж���ż: ";
    if (number & 1) { // ͨ����λ��ķ�ʽ�ж���ż
        cout << "The value " << number << " is an odd number\n";
    } else {
        cout << "The value " << number << " is an even number\n";
    }

    cout << "ͨ��ȡ��ķ�ʽ�ж���ż: ";
    if (number % 2) { // ͨ��ȡ��ķ�ʽ�ж���ż
        cout << "The value " << number << " is an odd number\n";
    } else {
        cout << "The value " << number << " is an even number\n";
    }
    return 0;
}