#include <cmath>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() {
    double input = 0.0, sum = 0.0, input_m = 0.0;
    int count = 0;
    vector<double> data;
    string unit;
    cout << "�����е��������Ϊm��λ��,�������ۼ�,��Ctrl+Z��Ϊ������\n";
    while (cin >> input >> unit) {
        if (unit == "cm") {
            input_m = input * 0.01;
        } else if (unit == "in") {
            input_m = input * 0.0254;
        } else if (unit == "ft") {
            input_m = input * 0.3048;
        } else {
            cout << "δ֪��λ\n";
        }
        data.push_back(input_m);
    }
    for (double x : data) {
        sum += x;
    }
    cout << "total sum: " << sum << "m \n";
    cout << "total amount: " << data.size() << " \n";
    return 0;
}
