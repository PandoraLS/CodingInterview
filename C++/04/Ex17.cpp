#include <bits/stdc++.h>
using namespace std;

struct choosen {
    int count;  //���ֵĴ���
    string value;  //ĳ���ַ���
};              //��¼ĳһֵ���ֵĴ���

int choose(vector<string>& L1) {
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
    vector<string> vs;
    string str,min,max,mode;
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
