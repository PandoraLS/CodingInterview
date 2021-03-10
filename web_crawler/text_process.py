import re
import json


def full2half(s):
    """全角转半角"""
    res = []
    for c in s:
        inside_code = ord(c)
        if inside_code == 12288:
            inside_code = 32
        elif 65281 <= inside_code <= 65374:
            inside_code -= 65248
        res.append(chr(inside_code))
    return ''.join(res)


def clean(s):
    s = re.sub(r'\s+', '', s)  # 去除空白符
    s = re.sub(r'\W+', '', s)  # 去除非字母数字
    s = full2half(s)  # 全角转半角
    return s


def to_unicode(s):
    """
    字符串转unicode编码
    :param s:
    :return:
    """
    return str(json.dumps(s))


if __name__ == '__main__':
    print('９月７日', '--->', full2half('９月７日'))
    print('haha#000我?·`/,./、】９月７日【hehe', '--->', clean('haha#000我?·`/,./、】９月７日【hehe'))
    print('哈哈xx·。8', '--->', to_unicode('哈哈xx·。8'))