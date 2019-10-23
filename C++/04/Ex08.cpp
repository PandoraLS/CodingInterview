#include <math.h>
#include <iostream>
using namespace std;
int main(void) {
    int grid = 0, grid_rice = 0, all_rice = 0;
    cout << "请输入发明人至少要获得的米粒数量：\n";
    int rice_num;
    cin >> rice_num;
    do {
        grid_rice = pow(2, grid);
        all_rice += grid_rice;
        grid++;
    } while (all_rice <= rice_num);
    cout << "共需 " << grid << " 个格子, " << all_rice << " 粒米\n";
    return 0;
}