#include <iostream>
using namespace std;
int square(int v) {
    int v2 = 0;
    for (int i = 0; i < v; i++) {
        v2 += v;
    }
    return v2;
}
int main() {
    for (int i = 0; i < 10; i++) {
        cout << i << "\t" << square(i) << "\n";
    }
    return 0;
}