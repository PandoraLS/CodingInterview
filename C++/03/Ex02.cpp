#include <stdio.h>
#include <iostream>
using namespace std;
int main() {
    double mile = 0.0;
    cout << "Ӣ��תΪ����, ������Ӣ������ ";
    while (cin >> mile) {
        cout << mile << " mile = " << mile * 1.609 << " km\n";
    }
    return 0;
}