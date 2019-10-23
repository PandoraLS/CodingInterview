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
    cout << "64个格子可以放置 " << all_rice << " 个米粒\n";

    // int的范围太大了，半天算不出来结果，所以修改为了short
    cout << "发明人至少要获得的米粒数量为 short 范围 " << (numeric_limits<short>::max)() << " 时\n";
    grid      = 0;
    grid_rice = 0;
    all_rice  = 0;
    do {
        grid_rice = pow(2, grid);
        all_rice += grid_rice;
        grid++;
    } while (all_rice <= (numeric_limits<short>::max)());  //int范围
    cout << "共需 " << grid << " 个格子, " << all_rice << " 粒米\n";

    return 0;
}