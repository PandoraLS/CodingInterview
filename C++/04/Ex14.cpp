#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;
// ������ɫ��ѡɸ����
// ��1���Ȱ�1ɾ�����ֽ���ѧ��1�Ȳ�������Ҳ���Ǻ�����
// ��2����ȡ�����е�ǰ��С����2��Ȼ���2�ı���ɾȥ
// ��3����ȡ�����е�ǰ��С����3��Ȼ���3�ı���ɾȥ
// ��4����ȡ�����е�ǰ��С����5��Ȼ���5�ı���ɾȥ
// ��5����������ֱ������ķ�Χ�����е�����ɾ�����ȡ

int main(void) {
    int n;
    cout << "���뷶Χ n ��\n";
    cin >> n;
    int* a = new int[n];
    for (int i = 0; i < n; i++) {
        a[i] = i;
    }
    for (int i = 2; i < sqrt(double(n)); i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[j] != 0 && a[j] % i == 0)
                a[j] = 0;
        }
    }
    cout << "��Χ " << n << " �ڵ�����Ϊ: \n";
    for (int i = 2; i < n; i++) {
        if (a[i] != 0)
            cout << a[i] << " ";
    }
    return 0;
}