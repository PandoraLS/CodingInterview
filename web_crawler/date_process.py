import re
from datetime import datetime, timedelta


time_format = '%Y-%m-%d'


def days_between(T_begin, T_end):
    """
    格式如下
    :param T_begin: 2018-01-01
    :param T_end:  2018-01-01
    :return:
    """
    b = datetime.strptime(T_begin, time_format)
    e = datetime.strptime(T_end, time_format)
    return (e - b).days


def calu_begin_date(T_now, before_days):
    """
    格式如下
    :param T_now: 2018-09-30
    :param before_days: 30
    :return: 2018-08-31
    """
    now = datetime.strptime(T_now, time_format)
    res = now - timedelta(days=before_days)
    return res.strftime(time_format)


def parse_time(t):
    res = ''
    mat = re.search(r'(\d{4}-\d{1,2}-\d{1,2})', t)
    if mat:
        res = mat.group(0)
    return res