// �ο����ӣ�https://blog.csdn.net/hello_worlden/article/details/47761371
// ʹ�ýṹ������¼����

#include <bits/stdc++.h>
using namespace std;

struct choosen {
    int count;  //���ֵĴ���
    int value;  //ֵ
};              //��¼ĳһֵ���ֵĴ���

int choose(vector<int>& L1) {
    sort(L1.begin(), L1.end()); //��L1����С�����������
    choosen Mode, Temp; // Mode�����������ս����Temp�����洢�м���
    Mode.count = 0;
    Mode.value = 0; //Mode��ʼ��
    Temp.count = 1; 
    Temp.value = L1.front(); //Temp��ʼ�����ӵ�һ��Ԫ�ؿ�ʼ
    for (int i = 0; i < L1.size() - 1; i++) {
        if (L1.at(i) == L1.at(i + 1)) //������������һ
            Temp.count++;
        else {
            if (Temp.count > Mode.count)
                Mode = Temp;
            Temp.count = 1;
            Temp.value = L1.at(i + 1);
        }
    }
    if (Temp.count > Mode.count)
        Mode = Temp;
    return Mode.value;
}

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
    min  = v[0];
    max  = v[v.size() - 1];
    mode = choose(v);
    cout << "\n���ֵ��" << max << "\n"
         << "��Сֵ��" << min << "\n"
         << "������ " << mode << endl;
    return 0;
}
