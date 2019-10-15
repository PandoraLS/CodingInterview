#include <iostream>
using namespace std;
int main() {
    char ch = 'a';
    while (ch <= 'z') {
        cout << ch << "  " << int(ch) << " \n";
        ch = char(ch + 1);
    }
    return 0;
}