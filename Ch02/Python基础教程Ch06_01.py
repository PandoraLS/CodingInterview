# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 16:04
# @Author  : Li Sen

def lookup(data, label, name):
    '返回data中对应label的name'
    return data[label].get(name)
    

def store(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:names.insert(1,'') # 如果名+姓只有两个单词，
        labels = 'first', 'middle', 'last'
        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
                
if __name__ == "__main__":
    Mynames = {}
    init(Mynames)
    store(Mynames, 'Magnus Lie Hetland')
    print(lookup(Mynames, 'middle', 'Lie'))
    