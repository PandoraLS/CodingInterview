#include <iostream>
using namespace std;
int main() {
    cout << "ÊäÈë×Ö·û´®£º" << endl;
    string str;
    while (cin >> str) {
        if (str == "one") {
            cout << "1\n";
        } else if (str == "two") {
            cout << "2\n";
        } else if (str == "three") {
            cout << "3\n";
        } else if (str == "four") {
            cout << "4\n";
        } else {
            cout << "not a number computer know\n";
        }
    }
    return 0;
}