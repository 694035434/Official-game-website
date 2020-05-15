from database.db_util import Db_util
class Hero():
    def __init__(self):
        self.db=Db_util()
        self.conn=self.db.conn
        self.cursor=self.db.cursor
    def insert(self,name,img,skill,story):
        sql="insert into t_hero(h_name,h_photo,h_skill,h_story) VALUES ('%s','%s','%s','%s')"%(name,img,skill,story)
        v = self.cursor.execute(sql)
        self.conn.commit()
        self.db.close()
        return v
    def hero_select(self):
            sql = "SELECT * FROM t_hero"
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            # for r1 in result:
            self.conn.commit()
            self.db.close()
            return result
    def hero_select_one(self,id):
            sql = "SELECT * FROM t_hero WHERE h_id=%d"%(int(id))
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            # for r1 in result:
            self.conn.commit()
            self.db.close()
            return result
    def select_limit(self):
        sql="select * from t_hero limit 4"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        # for r1 in result:
        self.conn.commit()
        self.db.close()
        return result