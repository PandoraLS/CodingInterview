#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    vector<string> vs = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    vector<int> vi    = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    string str, num_to_str;
    int str_to_num, num;
    cout << "拼写与数字转换\n";
    do {
        cout << "输入拼写：\n";
        cin >> str;
        for (int i = 0; i < 10; i++) {
            if (str == vs[i]) {
                str_to_num = vi[i];
                break;  //找到对应的数后，就退出当前for循环
            } else {
                str_to_num = -1;
            }
        }
        cout << str << " 对应的数字为 " << str_to_num << " \n";
        cout << "输入数字：\n";
        cin >> num;
        for (int i = 0; i < 10; i++) {
            if (num == vi[i]) {
                num_to_str = vs[i];
                break;
            } else {
                num_to_str = "error!";
            }
        }
        cout << num << " 对应的拼写为 " << num_to_str << " \n\n";
    } while (true);
    return 0;
}
