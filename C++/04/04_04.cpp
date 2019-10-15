#include <iostream>
using namespace std;
int main() {
    for (char ch = 'a'; ch <= 'z'; ch = char(ch + 1)) {
        cout << ch << "  " << int(ch) << " \n";
    }
    return 0;
}