#include <math.h>
#include <iostream>
using namespace std;
int main(void) {
    int grid = 0, grid_rice = 0, all_rice = 0;
    cout << "�����뷢��������Ҫ��õ�����������\n";
    int rice_num;
    cin >> rice_num;
    do {
        grid_rice = pow(2, grid);
        all_rice += grid_rice;
        grid++;
    } while (all_rice <= rice_num);
    cout << "���� " << grid << " ������, " << all_rice << " ����\n";
    return 0;
}