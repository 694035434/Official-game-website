from flask import Flask,render_template,request,Blueprint
from database.db_user import User
from database.db_user_manager import  manager
user_blue=Blueprint("user_model",__name__)

# 登录页面
@user_blue.route("/login")
def login():
    return render_template("login.html")
# 登录处理
@user_blue.route("/login_pro",methods=['POST','GET'])
def login_pro():
    if request.method=="GET":
        user=request.args.get("user")
        pwd=request.args.get("pwd")
        db=User()
        result=db.select(user,pwd)
        if str(result)=="1":
            return "T"
        elif result=="manager":
            return "M"
        else:
            return "F"

# 注册页面
@user_blue.route("/register")
def register():
    return render_template("register.html")
# 处理注册内容
@user_blue.route('/register_pro',methods=["POST","GET"])
def register_pro():
    if request.method=="GET":
        user=request.args.get('user')
        pwd = request.args.get('pwd')
        tel = request.args.get('tel')
        db=User()
        result=db.insert(user,pwd,tel)
        if result>0:
            return "T"
        else:
            return "F"
# 用户删除
@user_blue.route("/user_del", methods=['POST', 'GET'])
def user_del():
    if request.method == 'GET':
        userid = request.args.get('userid')
        # print(userid)
        db = manager()
        db.delete(int(userid))
        db = manager()
        result = db.select_all()
        return render_template("user_manager.html", u_result=result)

# 用户中心
@user_blue.route("/user_center", methods=['POST', 'GET'])
def user_center():
    if request.method == 'GET':
        u_name = request.args.get('u_name')
        # print(userid)
        db = User()
        result=db.user_search(u_name)
        return render_template("user_center.html", u_result=result)