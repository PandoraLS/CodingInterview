#include <math.h>
#include <iostream>
#include <limits>
using namespace std;
int main(void) {
    int grid = 0, grid_rice = 0, all_rice = 0;
    for (int i = 0; i < 64; i++) {
        grid_rice = pow(2, i);
        all_rice += grid_rice;
    }
    cout << "64�����ӿ��Է��� " << all_rice << " ������\n";

    // int�ķ�Χ̫���ˣ������㲻��������������޸�Ϊ��short
    cout << "����������Ҫ��õ���������Ϊ short ��Χ " << (numeric_limits<short>::max)() << " ʱ\n";
    grid      = 0;
    grid_rice = 0;
    all_rice  = 0;
    do {
        grid_rice = pow(2, grid);
        all_rice += grid_rice;
        grid++;
    } while (all_rice <= (numeric_limits<short>::max)());  //int��Χ
    cout << "���� " << grid << " ������, " << all_rice << " ����\n";

    return 0;
}