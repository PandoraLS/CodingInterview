#include <ctime>
#include <iostream>
using namespace std;

int main(void) {
    int n, num, count = 1;
    srand(time(0));
    num = rand() % 100;
    do {
        cout << "��һ�� 100 ���ڵ�����";
        cin >> n;
        if (n == num)
            break;
        else if (n > num)
            cout << "���ˣ�" << endl;
        else
            cout << "С�ˣ�" << endl;
        count++;
    } while (true);
    cout << "���� " << count << " �Σ��¶��ˣ�" << endl;
    return 0;
}
