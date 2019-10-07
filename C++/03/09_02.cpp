#include <stdio.h>
#include <iostream>
using namespace std;
int main() {
    double d = 0;
    while (cin >> d) {
        int i  = d;
        char c = i;
        int i2 = c;
        cout << "d==" << d
             << " i==" << i
             << " i2==" << i2
             << " char(" << c << ")\n";
    }

    return 0;
}