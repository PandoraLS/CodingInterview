#include <iostream>
using namespace std;
int main() {
    constexpr double JPY_USD = 0.0093;  //日元汇率
    constexpr double EUR_USD = 1.0963;  //欧元汇率
    constexpr double GBP_USD = 1.2325;  //英镑汇率
    double number            = 1;
    char unit                = ' ';
    cout << "Please enter a number followed by a unit (J or E or G): \n";
    cin >> number >> unit;
    switch (unit) {
        case 'J':
            cout << number << " JPY = " << JPY_USD * number << " USD\n";
            break;
        case 'E':
            cout << number << " EUR = " << EUR_USD * number << " USD\n";
            break;
        case 'G':
            cout << number << " GBP = " << GBP_USD * number << " USD\n";
            break;
        default:
            cout << "dont know!\n";
            break;
    }
    return 0;
}