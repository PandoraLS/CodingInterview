#include <iostream>
#include <tuple>
using namespace std;

std::tuple<int, int> create_a_tuple(int a, int b) {
    //���ڽ�����Ԫ�����tuple
    return std::make_tuple(a, b);
}

auto compare(int a, int b) {
    int max = 0, min = 0;
    if (a >= b) {
        max = a, min = b;
    } else {
        max = b, min = a;
    }
    auto data = create_a_tuple(max, min);
    return data;
}

int main() {
    int a = 0, b = 0, c = 0;
    cout << "��������������ֵ��";
    cin >> a >> b >> c;
    int max = 0, mid = 0, min = 0;
    auto Data = compare(a, b);
    max       = std::get<0>(Data);
    min       = std::get<1>(Data);
    if (c >= max) {
        mid = max;
        max = c;
    } else if (c < min) {
        mid = min;
        min = c;
    } else {
        mid = c;
    }
    std::cout << "����С�����˳������� " << min << ", " << mid << ", " << max;
    return 0;
}