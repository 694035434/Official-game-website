from database.db_util import Db_util
class manager():
    def __init__(self):
        self.db=Db_util()
        self.conn=self.db.conn
        self.cursor=self.db.cursor
    def user_select(self, username):
            if username:
                sql = "SELECT * FROM t_user WHERE  u_name LIKE '%" + username + "%'"
            else:
                sql = "SELECT * FROM t_user"
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            # for r1 in result:
            self.conn.commit()
            self.db.close()
            return result
    def delete(self,id):
        sql = "delete from t_user WHERE u_id=%d" % (id)
        v = self.cursor.execute(sql)
        self.conn.commit()
        self.db.close()
        return v
    def select_all(self):
        sql = 'SELECT * FROM t_user'
        self.cursor.execute(sql)
        v = self.cursor.fetchall()
        self.conn.commit()
        self.db.close()
        return v