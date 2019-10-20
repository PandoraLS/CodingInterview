#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int main() {
    vector<double> temps;
    double avg = 0.0, sum = 0.0, min = 0.0, max = 0.0;
    for (double temp; cin >> temp;) {
        temps.push_back(temp);
    }
    sort(temps.begin(), temps.end());
    min = temps[0];
    max = temps[temps.size() - 1];
    for (double x : temps) {
        sum += x;
    }
    cout << "sum: " << sum << " \n";
    cout << "avg: " << sum / temps.size() << " \n";
    cout << "min: " << min << " \n";
    cout << "max: " << max << " \n";
    return 0;
}
