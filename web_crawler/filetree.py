"""
输出文件夹的目录树
"""


import os
import os.path
import sys

BRANCH = '├─'
LAST_BRANCH = '└─'
TAB = '│  '
EMPTY_TAB = '   '
IGNORE_DIRS = {'.git', '.idea'}
IGNORE_FILES = {'filetree.py'}


def get_dir_list(path, placeholder=''):
    folder_list = [folder for folder in os.listdir(path) if os.path.isdir(os.path.join(path, folder)) and folder not in IGNORE_DIRS]
    file_list = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)) and file not in IGNORE_FILES]
    result = ''
    for folder in folder_list[:-1]:
        result += placeholder + BRANCH + folder + '\n'
        result += get_dir_list(os.path.join(path, folder), placeholder + TAB)
    if folder_list:
        result += placeholder + (BRANCH if file_list else LAST_BRANCH) + folder_list[-1] + '\n'
        result += get_dir_list(os.path.join(path, folder_list[-1]), placeholder + (TAB if file_list else EMPTY_TAB))
    for file in file_list[:-1]:
        result += placeholder + BRANCH + file + '\n'
    if file_list:
        result += placeholder + LAST_BRANCH + file_list[-1] + '\n'
    return result


if __name__ == '__main__':
    doc = """
参数格式1：python filetree.py src_dir             # 将src_dir的目录树输出到终端
参数格式2：python filetree.py src_dir dest_file   # 将src_dir的目录树输出到dest_file
示例：     python filetree.py C:\Desktop D:\filetree.txt
路径不含空格
    """
    if len(sys.argv) == 1:
        print(doc)
    elif len(sys.argv) == 2:  # 标准输出
        print(get_dir_list(sys.argv[1]))
    elif len(sys.argv) == 3:  # 输出到文件
        with open(sys.argv[2], 'xt', encoding='utf-8') as f:
            print(get_dir_list(sys.argv[1]), file=f)
    else:
        print('！！！参数错误')
        print(doc)
