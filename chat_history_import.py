# -*- coding:utf-8 -*-

import re

# from mysql_orm import SQLStore

# s = SQLStore()

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

def sql_str_conversion(str):
    return "'" + str + "'"

def main():
    file_path = "./data/dear_chat_record.txt"
    for record in open(file_path, 'r').readlines():
        send_key = "我{0}发送".format(" " * 23)
        if send_key in record:
            position = record.index(send_key)
            desc_content = record[0:position + 3 + 23 + 6]
            name = sql_str_conversion("董浩" if get_name(desc_content) else None)
            record_type = 0
            record_time = sql_str_conversion(get_record_time(desc_content))
            content = sql_str_conversion(record[position + 3 + 23 + 6:-1].lstrip())

            # TODO：或许存变
            s.insert(tab_name='chat_record_for_dear',
                     name=name,
                     record_type=record_type,
                     record_time=record_time,
                     content=content)

        receive_key = "王懒懒{0}接收".format(" " * 19)
        if receive_key in record:
            position = record.index(receive_key)
            desc_content = record[0:position + 9 + 19 + 6]
            name = sql_str_conversion("星儿" if get_name(desc_content) else None)
            record_type = 1
            record_time = sql_str_conversion(get_record_time(desc_content))
            content = sql_str_conversion(record[position + 9 + 19 + 6:-1].lstrip())

            # TODO：或许存变
            s.insert(tab_name='chat_record_for_dear',
                     name=name,
                     record_type=record_type,
                     record_time=record_time,
                     content=content)


if __name__ == "__main__":
    main()

