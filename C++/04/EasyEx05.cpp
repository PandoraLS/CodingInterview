#include <cmath>
#include <iostream>
using namespace std;
int main() {
    double a = 0.0, b = 0.0;
    while (cin >> a >> b) {
        if (a >= b) {
            cout << "the smaller value is " << b << "\n";
            cout << "the larger value is " << a << "\n";
        } else {
            cout << "the smaller value is " << a << "\n";
            cout << "the larger value is " << b << "\n";
        }
        if (fabs(a - b) < 0.01) {
            cout << "the numbers are almost equal \n";
        }
    }
    return 0;
}