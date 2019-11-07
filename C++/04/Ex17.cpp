#include <bits/stdc++.h>
using namespace std;

struct choosen {
    int count;  //出现的次数
    string value;  //某个字符串
};              //记录某一值出现的次数

int choose(vector<string>& L1) {
    sort(L1.begin(), L1.end()); //对L1按从小到大进行排序
    choosen Mode, Temp; // Mode用来保存最终结果，Temp用来存储中间结果
    Mode.count = 0;
    Mode.value = 0; //Mode初始化
    Temp.count = 1; 
    Temp.value = L1.front(); //Temp初始化，从第一个元素开始
    for (int i = 0; i < L1.size() - 1; i++) {
        if (L1.at(i) == L1.at(i + 1)) //若相等则次数加一
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
    cout << "输入一组int数据:\n";
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
    cout << "\n最大值：" << max << "\n"
         << "最小值：" << min << "\n"
         << "众数： " << mode << endl;
    return 0;
}
