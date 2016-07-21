# coding=utf8

from sys import version_info as PY_VER

PY3 = PY_VER[0] == 3


def int_with_commas(x):
    # Use commmas to separate numbers into groups of three digits
    if type(x) not in [type(0), type(0L)]:
        raise TypeError("Parameter must be an integer.")
    if x < 0:
        return '-' + intWithCommas(-x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ",%03d%s" % (r, result)
    return "%d%s" % (x, result)

print int_with_commas(987642)
