#include <iostream>
#include <vector>
using namespace std;
void getPrime(int n, vector<int>& vi) {
    // n : ��Χ n
    // ɸѡ������ɸѡ������С����ɸȥһ����֪���������б���������ɾ���ɱ�2������3�����������������֣�ʣ�µ���Ϊ����
    int i, j;
    bool m;
    for (i = 2; i <= n; i++) {
        m = true;  // �ȼ���iΪ����, ��ʱm = true;
        for (j = 2; j < i; j++) {
            if (i % j == 0) { // �������i������������ô m = false;
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
    cout << "���뷶Χ n ��\n";
    cin >> num;
    getPrime(num, vi);
    cout << "��Χ n �ڵ�����Ϊ: \n";
    for (vector<int>::iterator it = vi.begin(); it != vi.end(); it++) {
        cout << *it << " ";
    }
    cout << endl;
    return 0;
}
