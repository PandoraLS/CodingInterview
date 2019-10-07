#include <cmath>
#include <iostream>
using namespace std;

int main() {
    cout << "enter a float value: ";
    int n;
    cin >> n;
    cout << "n == " << n
         << "\nn+1 == " << n + 1
         << "\nthree times n == " << 3 * n
         << "\ntwice n == " << n + n
         << "\nn squared == " << n * n
         << "\nhalf of n == " << n / 2
         << "\nsquare root of n == " << sqrt(n)
         << "\n";
    return 0;
}

// int main()
// {
//     cout << "enter a float value: ";
//     double n;
//     cin >> n;
//     cout << "n == " << n
//          << "\nn+1 == " << n + 1
//          << "\nthree times n == " << 3 * n
//          << "\ntwice n == " << n + n
//          << "\nn squared == " << n * n
//          << "\nhalf of n == " << n / 2
//          << "\nsquare root of n == " << sqrt(n)
//          << "\n";
//     return 0;
// }
