import pymysql
# 数据库通用类

class Db_util():
   #初始化连接对象
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root',
                                    password='uf5m123456', database='db_webproject',charset='utf8')
        self.cursor=self.conn.cursor()
    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()