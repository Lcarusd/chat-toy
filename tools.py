# -*- coding:utf-8  -*-

import os


def is_dir_path(dir_path):
    '''判断文件夹路径是否存在,否则创建'''
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

