from math import floor, ceil

stu_list = [['201801', 'zhangyi'], ['201802', 'zhanger'], ['201803', 'zhangsan'], ['201804', 'zhangsi'],
            ['201805', 'wangyi'], ['201806', 'wanger'], [
                '201807', 'wangsan'], ['201808', 'wangsi'], ['201809', 'liyi'],
            ['201810', 'lier'], ['201811', 'lisan'], ['201812', 'lisi'], [
                '201813', 'zhaoyi'], ['201814', 'zhaoer'],
            ['201815', 'zhaosan'], ['201816', 'zhaosi'], ['201817', 'zhouyi'], ['201818', 'zhouer'], ['201819', 'zhousan'], ['201820', 'zhousi']]


def binary_search(keyword, data):
    if len(data) == 0:
        return None

    central = len(data) / 2
    central_ceil = ceil(central)

    if keyword == data[central_ceil - 1][0]:
        return ''.join(data[central_ceil - 1])

    if keyword > data[central_ceil - 1][0]:
        return binary_search(keyword, data[central_ceil:])

    if keyword < data[central_ceil - 1][0]:
        return binary_search(keyword, data[:central_ceil - 1])


stu_num = input()
result = binary_search(stu_num, stu_list)
print(result)
