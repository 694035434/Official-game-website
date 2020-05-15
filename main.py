from flask import Flask,render_template,request
from model.User_model import *
from model.news_model import *
from model.ac_model import *
from model.hero_model import *
app=Flask(__name__)
app.register_blueprint(user_blue)
app.register_blueprint(news_blue)
app.register_blueprint(ac_blue)
app.register_blueprint(hero_blue)

# 简首页
@app.route("/")
def xxx():
    # return render_template("simple_index.html")
    return render_template("simple_index.html")

# 主页
@app.route("/index")
def index():
    db = Activity()
    result_ac = db.select_limit()
    news=Newsmanager()
    result_news1=news.select_limit_first()
    # print(result_news1)
    news = Newsmanager()
    result_news2 = news.select_limit_second()
    db = Activity()
    result_ac2 = db.select_limit_one()
    db=Hero()
    hero=db.select_limit()
    # print(hero)
    return render_template("index.html",ac_result=result_ac,news_result=result_news1,news_result2=result_news2,ac_result2=result_ac2,hero_img=hero)

# 管理页面
@app.route("/server")
def server():
    return render_template("server.html")

#个人中心管理
@app.route("/user_manager",methods=['POST','GET'])
def user_manager():
    return render_template("user_manager.html")

#个人中心用户查询
@app.route("/user_search",methods=['POST','GET'])
def user_search():
    if request.method=="GET":
        username=request.args.get("username")
        db=manager()
        result=db.user_select(username)
        return render_template("user_manager.html", u_result=result)

#新闻中心管理
@app.route("/news_manager")
def news_manager():
    return render_template("news_manager.html")

#活动中心管理
@app.route("/activity_manager")
def activity_manager():
    return render_template("activity_manager.html")

#英雄资料管理
@app.route("/hero_manager")
def hero_manager():
    return render_template("hero_manager.html")


if __name__ == '__main__':
    app.run()

