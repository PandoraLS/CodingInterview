/*
 * @Author: seenli
 * @Date: 2021-01-11 21:43:18
 * @LastEditors: seenli
 * @LastEditTime: 2021-03-11 00:56:57
 * @FilePath: \C++\demo.cpp
 * @Description: LeetCode Hot 100
 */

// https://blog.csdn.net/fendoubasaonian/article/details/49662393

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int Fibonacci(int n) {
        int n1 = 0;
        int n2 = 1;
        int ni;
        if (n <= 0) return 0;
        if (n == 1) return 1;

        for(int i = 2; i <= n; i++) {
            ni = n1 + n2;
            n1 = n2;
            n2 = ni;
        }
        return ni;

    }
};

int main()
{
    Solution Fbnc;
    cout<<"Fbnq[10]=  "<<Fbnc.Fibonacci(10)<<endl;  //类是抽象化的，你要定义一个实例对象，通过实例调用；

    Solution *Fbnc1= new Solution();
    cout<<"Fbnq[5]=  "<<Fbnc1->Fibonacci(5)<<endl;
    delete Fbnc1;
    system("pause");
    return 0;
}
