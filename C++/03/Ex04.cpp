#include <stdio.h>
#include <iostream>
using namespace std;
int main() {
    int val1 = 0, val2 = 0;
    int max = 0, min = 0;
    int sum = 0, difference = 0, product = 0, quotient = 0;
    cout << "请输入两个数：";
    cin >> val1;
    cin >> val2;
    if (val1 >= val2) {
        max = val1;
        min = val2;
    } else {
        max = val2;
        min = val1;
    }
    cout << "max: " << max
         << " \nmin: " << min
         << " \nsum: " << val1 + val2
         << " \ndifference: " << max - min
         << " \nproduct: " << max * min
         << " \nquotient: " << max / min << '\n';
    return 0;
}