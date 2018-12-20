# -*- coding:utf-8 -*-

import re


# 提取聊天时间子串
def get_record_time(desc_content):
    r = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
    search = re.search(r, desc_content)
    return search.group(0)

# 提取姓名子串
def get_name(desc_content):
    r = r"\s{3}我\s{3}|\s{3}王懒懒\s{3}"
    search = re.search(r, desc_content)
    return search.group(0).lstrip().rstrip()

file_path = "./data/dear_chat_record.txt"
for record in open(file_path, 'r').readlines():
    # 子串分离
    send_key = "我{0}发送".format(" " * 23)
    if send_key in record:
        position = record.index(send_key)
        desc_content = record[0:position + 3 + 23 + 6]
        name = get_name(desc_content)
        record_type = 0
        record_time = get_record_time(desc_content)
        content = record[position + 3 + 23 + 6:-1].lstrip()

    receive_key = "王懒懒{0}接收".format(" " * 19)
    if receive_key in record:
        position = record.index(receive_key)
        desc_content = record[0:position + 9 + 19 + 6]
        name = get_name(desc_content)
        record_type = 1
        record_time = get_record_time(desc_content)
        content = record[position + 9 + 19 + 6:-1].lstrip()
