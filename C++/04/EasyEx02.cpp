#include <iostream>
using namespace std;
int main() {
    int a = 0, b = 0;
    while (cin >> a >> b) {
        if (a >= b) {
            cout << "the smaller value is " << b << "\n";
            cout << "the larger value is " << a << "\n";
        } else {
            cout << "the smaller value is " << a << "\n";
            cout << "the larger value is " << b << "\n";
        }
    }
    return 0;
}