# -*- coding:utf-8 -*-

# import pymysql
#
#
# class SQLStore(object):
#
#     def create_connection(self):
#         conn = pymysql.Connect(
#             host='localhost',
#             port=3306,
#             user='root',
#             passwd='19950925',
#             db='chattoy',
#             charset='utf8',
#             cursorclass = pymysql.cursors.DictCursor
#         )
#         cursor = conn.cursor()  # 获取cursor
#         return cursor, conn
#
#     def insert_data(self):
#         try:
#             cursor, conn = self.create_connection()
#             cursor.execute('insert into {0}(name, record_type, record_time, content) '
#                            'values ("我", 0, "2018-07-03 22:42:22", "哈哈哈") '.format('chat_record_for_dear'))
#             # 提交执行
#             conn.commit()
#         except Exception as e:
#             # 如果执行sql语句出现问题，则执行回滚操作
#             conn.rollback()
#             print(e)
#         finally:
#             cursor.close()
#             conn.close()