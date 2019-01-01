# -*- coding:utf-8 -*-

# import pymysql
# #
# #
# # class SQLStore(object):
# #
# #     def __init__(self):
# #         self.db_conn = pymysql.Connect(    # 打开数据库连接
# #             host='localhost',
# #             port=3306,
# #             user='root',
# #             passwd='19950925',
# #             db='chattoy',
# #             charset='utf8',
# #             cursorclass = pymysql.cursors.DictCursor
# #         )
# #         self.cursor = self.db_conn.cursor()    # 游标对象
# #
# #     def insert(self, tab_name, name, record_type, record_time, content):
# #         try:
# #             sql = 'insert into {0}(name, record_type, record_time, content) values ({1}, {2}, {3}, {4})'.format(tab_name, name, record_type, record_time, content)
# #             print (sql)
# #             self.cursor.execute(sql)
# #             self.db_conn.commit()
# #         except Exception as e:
# #             self.db_conn.rollback()
# #             print(e)
# #         finally:
# #             pass
# #             # self.cursor.close()
# #             # self.db_conn.close()
# #
# #     def get_record(self):
# #         self.cursor.execute('select * from chat_record_for_dear order by id desc limit 1')
# #         self.db_conn.commit()
# #         results = self.cursor.fetchall()
# #         self.db_conn.close()
# #         return results[0]
# #
# #     def del_record(self):
# #         cursor, conn = self.create_connection()
# #         cursor.execute('delete from chat_record_for_dear where id = 1')
# #         conn.commit()
# #         conn.close()
# #
# #     def update_record(self, tab_name, content, id):
# #         self.cursor.execute('update {0} set content={1} where id={2}'.format(tab_name, content, id))
# #         self.db_conn.commit()
# #         self.db_conn.close()



# s = SQLStore()
# s.insert(
#     tab_name='chat_record_for_dear',
#     name="'李四搜搜索索'",
#     record_type=1,
#     record_time="'2018-07-02 22:42:22'",
#     content="'王二卖瓜哈哈哈哈哈哈哈，我也不知道'")
# s.update_record('chat_record_for_dear', "'测试已'", 1)