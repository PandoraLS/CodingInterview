#include <cmath>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() {
    double input = 0.0;
    string unit;
    cout << "将所有的输出换算为m单位制：\n";
    while (cin >> input >> unit) {
        if (unit == "cm") {
            cout << input << unit << " == " << input * 0.01 << "m\n";
        } else if (unit == "in") {
            cout << input << unit << " == " << input * 0.0254 << "m\n";
        } else if (unit == "ft") {
            cout << input << unit << " == " << input * 0.3048 << "m\n";
        } else {
            cout << "未知单位\n";
        }
    }
    return 0;
}
