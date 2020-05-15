from database.db_util import Db_util
class Newsmanager():
    def __init__(self):
        self.db = Db_util()
        self.conn = self.db.conn
        self.cursor = self.db.cursor

    def insert(self, name, time,n_class,introduce):
        sql = "insert into t_news (n_name,n_time,n_class,n_introduce) VALUES ('%s','%s','%s','%s')" % (
            name, time, n_class, introduce)
        v = self.cursor.execute(sql)
        self.conn.commit()
        self.db.close()
        return v

    def news_select(self):
            sql = "SELECT * FROM t_news"
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            # for r1 in result:
            self.conn.commit()
            self.db.close()
            return result
    def select_limit_first(self):
        sql="select * from t_news limit 1"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # for r1 in result:
        self.conn.commit()
        self.db.close()
        return result
    def select_limit_second(self):
        sql="select * from t_news limit 1,1"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # for r1 in result:
        self.conn.commit()
        self.db.close()
        return result
    def news_select_one(self,id):
        sql = "SELECT * FROM t_news WHERE n_id=%d"%(int(id)+1)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # for r1 in result:
        self.conn.commit()
        self.db.close()
        return result
    def select_class(self,n_class):
        sql = "SELECT * FROM t_news WHERE n_class='%s'"%(n_class)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # for r1 in result:
        self.conn.commit()
        self.db.close()
        return result