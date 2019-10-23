#include <stdio.h>
#include <sys/time.h>  //添加头文件
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

int64_t getCurrentTime() {
    //直接调用这个函数就行了，返回值最好是int64_t，long long应该也可以
    //C/C++获取系统时间戳，精确到毫秒
    struct timeval tv;
    gettimeofday(&tv, NULL);  //该函数在sys/time.h头文件中
    return tv.tv_sec * 1000 + tv.tv_usec / 1000;
}

int main(void) {
    vector<string> vs = {"stone", "scissors", "cloth"};
    int random_num, index;
    do {
        cout << "随意输入一个数（只是起到暂停作用）：\n";
        cin >> random_num;
        srand(abs(getCurrentTime()) + random_num); //使用abs是防止结果中的 负 值
        index = rand() % 3;
        cout << vs[index] << " \n";
    } while (true);
    return 0;
}
