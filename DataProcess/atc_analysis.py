# -*- coding: utf-8 -*-
# Author：sen
# Date：2020/2/29 22:36

def read_data():
    file = "C:\\Users\\M\\Desktop\\data2\\error_list_test_val_proc.csv"
    f = open(file)
    lines = f.readlines()
    new_file = []
    for line in lines:
        line = line.strip()
        tmp_line = line.split(',')
        new_line = tmp_line[0]+'\n' \
                    + 'trans: ' + tmp_line[3] + '\n' \
                    + 'refer: ' + tmp_line[4] + '\n' \
                    + 'WER: ' + tmp_line[2] + '     ' + 'CER: ' + tmp_line[1] + '\n\n'
        new_file.append(new_line)
        
    with open('error_list_test_val_proc_tmp.txt','w') as ff:
        for line in new_file:
            ff.write(line)
        
        
if __name__ == '__main__':
    read_data()