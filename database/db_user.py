from database.db_util import Db_util
class User():
    def __init__(self):
        self.db=Db_util()
        self.conn=self.db.conn
        self.cursor=self.db.cursor
    def insert(self,name,password,tel):
        sql = "insert into t_user (u_name,u_pwd,u_tel) VALUES ('%s','%s','%s')" % (
                name, password,tel)
        v = self.cursor.execute(sql)
        self.conn.commit()
        self.db.close()
        return v
    def select(self,user,pwd):
        sql = "SELECT * FROM t_user WHERE u_name='%s' and u_pwd='%s' " % (user,pwd)
        result=self.cursor.execute(sql)
        # 判断是否为管理员
        r1=self.cursor.fetchone()
        ismanager=r1[8]
        print(result)
        self.conn.commit()
        self.db.close()
        if ismanager==1:
            return "manager"
        else:
            return result
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
    def user_search(self, username):
            sql = "SELECT * FROM t_user WHERE u_name='%s'"%(username)
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            # for r1 in result:
            self.conn.commit()
            self.db.close()
            return result