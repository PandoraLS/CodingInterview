#include <cmath>
#include <iostream>
using namespace std;
int main() {
    double in  = 0.0;
    double min = in, max = in;
    while (cin >> in) {
        if (in < min) {
            min = in;
        }
        if (in >= max) {
            max = in;
        }
        cout << "the smaller so far " << min << "\n";
        cout << "the larger so far " << max << "\n";
    }
    return 0;
}
