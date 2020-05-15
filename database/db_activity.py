from database.db_util import Db_util
class Activity():
    def __init__(self):
        self.db=Db_util()
        self.conn=self.db.conn
        self.cursor=self.db.cursor
    def insert(self,name,time,img,introduce,bimg):
        sql="insert into t_activity(a_name,a_time,a_photo,a_introduce,a_detailed_photo) VALUES ('%s','%s','%s','%s','%s')"%(name,time,img,introduce,bimg)
        v = self.cursor.execute(sql)
        self.conn.commit()
        self.db.close()
        return v
    def ac_select(self):
            sql = "SELECT * FROM t_activity"
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            # for r1 in result:
            self.conn.commit()
            self.db.close()
            return result

    # 查询前三条
    def select_limit(self):
        sql="select * from t_activity limit 4"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # for r1 in result:
        self.conn.commit()
        self.db.close()
        return result
    def select_limit_one(self):
        sql="select * from t_activity limit 4,1"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # for r1 in result:
        self.conn.commit()
        self.db.close()
        return result
    def ac_select_one(self,id):
        sql="select * from t_activity WHERE a_id=%d"%(int(id)+1)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # for r1 in result:
        self.conn.commit()
        self.db.close()
        return result