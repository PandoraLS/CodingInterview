# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 18:54
# @Author  : sen

if __name__ == '__main__':
    n = input()
    les_start, les_end = [], []
    for i in range(int(n)):
        line = line.strip().split()
        les_start.append(line[0])
        les_end.append(line[-1])
    les_start = [int(_) for _ in les_start]
    les_end = [int(_) for _ in les_end]
    max_value = max(les_end)
    min_value = min(les_start)
    tmp = max_value - min_value
    cntArr = [0] * (max_value - min_value)
    for i in range(min_value, max_value):
        cnt = 0
        for j in range(int(n)):
            if i >= les_start[j] and i < les_end[j]:
                cnt += 1
        cntArr[i - min_value] = cnt

    minCnt = max(cntArr)
    print(str(minCnt))

