#include <stdio.h>
#include <sys/time.h>  //���ͷ�ļ�
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

int64_t getCurrentTime() {
    //ֱ�ӵ���������������ˣ�����ֵ�����int64_t��long longӦ��Ҳ����
    //C/C++��ȡϵͳʱ�������ȷ������
    struct timeval tv;
    gettimeofday(&tv, NULL);  //�ú�����sys/time.hͷ�ļ���
    return tv.tv_sec * 1000 + tv.tv_usec / 1000;
}

int main(void) {
    vector<string> vs = {"stone", "scissors", "cloth"};
    int random_num, index;
    do {
        cout << "��������һ������ֻ������ͣ���ã���\n";
        cin >> random_num;
        srand(abs(getCurrentTime()) + random_num); //ʹ��abs�Ƿ�ֹ����е� �� ֵ
        index = rand() % 3;
        cout << vs[index] << " \n";
    } while (true);
    return 0;
}
