from flask import Flask,render_template,request,Blueprint
from database.db_news_manager import Newsmanager
news_blue=Blueprint("news_model",__name__)
import os


# 新闻插入
@news_blue.route('/news_join',methods=["POST","GET"])
def news_join():
    if request.method=="GET":
        name=request.args.get('name')
        time= request.args.get('time')
        n_class= request.args.get('n_class')
        introduce = request.args.get('introduce')
        db=Newsmanager()
        result=db.insert(name,time,n_class,introduce)
        if result>0:
            return "T"
        else:
            return "F"

# 新闻查询
@news_blue.route('/news_query', methods=["POST", "GET"])
def news_query():
    if request.method=="GET":
        db=Newsmanager()
        result=db.news_select()
        db = Newsmanager()
        result_xw = db.select_class("新闻")
        db = Newsmanager()
        result_gg = db.select_class("公告")
        db = Newsmanager()
        result_hd = db.select_class("活动")
        return render_template("news.html",u_result=result,result_xw=result_xw,result_gg=result_gg,result_hd =result_hd )

# 新闻详细查询
@news_blue.route('/news_query_one', methods=["POST", "GET"])
def news_query_one():
    if request.method == "GET":
        id=request.args.get('id')
        db = Newsmanager()
        result = db.news_select_one(id)
        return render_template("news_introduce.html", u_result=result)