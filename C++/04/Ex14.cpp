#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;
// 埃拉托色尼选筛法：
// （1）先把1删除（现今数学界1既不是质数也不是合数）
// （2）读取队列中当前最小的数2，然后把2的倍数删去
// （3）读取队列中当前最小的数3，然后把3的倍数删去
// （4）读取队列中当前最小的数5，然后把5的倍数删去
// （5）如上所述直到需求的范围内所有的数均删除或读取

int main(void) {
    int n;
    cout << "输入范围 n ：\n";
    cin >> n;
    int* a = new int[n];
    for (int i = 0; i < n; i++) {
        a[i] = i;
    }
    for (int i = 2; i < sqrt(double(n)); i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[j] != 0 && a[j] % i == 0)
                a[j] = 0;
        }
    }
    cout << "范围 " << n << " 内的素数为: \n";
    for (int i = 2; i < n; i++) {
        if (a[i] != 0)
            cout << a[i] << " ";
    }
    return 0;
}