#include <iostream>
#include <vector>
using namespace std;
void getPrime(int n, vector<int>& vi) {
    // n : 范围 n
    // 筛选素数，筛选法，从小到大筛去一个已知素数的所有倍数。依次删除可被2整除，3整除。。。。的数字，剩下的则为素数
    int i, j;
    bool m;
    for (i = 2; i <= n; i++) {
        m = true;  // 先假设i为素数, 此时m = true;
        for (j = 2; j < i; j++) {
            if (i % j == 0) { // 如果发现i不是素数，那么 m = false;
                m = false;
                break;
            }
        }
        if (m) {
            vi.push_back(i);
            // cout << i << " ";
        }
    }
}

int main(void) {
    vector<int> vi;
    int num = 0;
    cout << "输入范围 n ：\n";
    cin >> num;
    getPrime(num, vi);
    cout << "范围 n 内的素数为: \n";
    for (vector<int>::iterator it = vi.begin(); it != vi.end(); it++) {
        cout << *it << " ";
    }
    cout << endl;
    return 0;
}
