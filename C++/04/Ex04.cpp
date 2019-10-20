#include <ctime>
#include <iostream>
using namespace std;

int main(void) {
    int n, num, count = 1;
    srand(time(0));
    num = rand() % 100;
    do {
        cout << "猜一个 100 以内的数：";
        cin >> n;
        if (n == num)
            break;
        else if (n > num)
            cout << "大了！" << endl;
        else
            cout << "小了！" << endl;
        count++;
    } while (true);
    cout << "历经 " << count << " 次，猜对了！" << endl;
    return 0;
}
