#include <iostream>
#include <vector>
using namespace std;
int main(void) {
    vector<string> vs = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    vector<int> vi    = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    string str, num_to_str;
    int str_to_num, num;
    cout << "ƴд������ת��\n";
    do {
        cout << "����ƴд��\n";
        cin >> str;
        for (int i = 0; i < 10; i++) {
            if (str == vs[i]) {
                str_to_num = vi[i];
                break;  //�ҵ���Ӧ�����󣬾��˳���ǰforѭ��
            } else {
                str_to_num = -1;
            }
        }
        cout << str << " ��Ӧ������Ϊ " << str_to_num << " \n";
        cout << "�������֣�\n";
        cin >> num;
        for (int i = 0; i < 10; i++) {
            if (num == vi[i]) {
                num_to_str = vs[i];
                break;
            } else {
                num_to_str = "error!";
            }
        }
        cout << num << " ��Ӧ��ƴдΪ " << num_to_str << " \n\n";
    } while (true);
    return 0;
}
