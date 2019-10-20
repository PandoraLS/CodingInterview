#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int main() {
    vector<double> temps;
    for (double temp; cin >> temp;) {
        temps.push_back(temp);
    }
    sort(temps.begin(), temps.end());

    if (temps.size() % 2) {
        // ÆæÊý
        cout << "Median temperature: " << temps[temps.size() / 2] << "\n";
    } else {
        cout << "Median temperature: " << (temps[temps.size() / 2] + temps[temps.size() / 2 - 1]) / 2.0 << "\n";
    }
    return 0;
}