#include <iostream>
#include<stdio.h>
using namespace std;
int main() {
    int a  = 20000;
    char c = a;
    int b  = c;
    if (a != b) {
        cout << "oops!: " << a << "!=" << b << '\n';
    } else {
        cout << "wow! We have large characters\n";
    }
    cout << b;
    return 0;
}