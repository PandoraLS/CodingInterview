#include <bits/stdc++.h>
using namespace std;

int main(void) {
    vector<int> v;
    int num = 0, max = 0, min = 0, mode = 0;
    cout << "����һ��int����:\n";
    while (cin >> num) {
        v.push_back(num);
    }
    sort(v.begin(), v.end());
    for (int x : v) {
        cout << x << " ";
    }
    // for (int x : v) {
    //     if (x > max)
    //         max = x;
    //     if (x < min)
    //         min = x;
    // }

    return 0;
}

// https://blog.csdn.net/hello_worlden/article/details/47761371
// TODO �ο����ӣ���ʱ�俴��