from flask import Flask,render_template,request,Blueprint
from database.db_hero import  Hero
hero_blue=Blueprint("hero_model",__name__)
import os
# 英雄发布
@hero_blue.route("/hero_manager_pro",methods=["POST","GET"])
def hero_manager_pro():
    if request.method=="POST":
        v_name=request.form["h_name"]
        v_img = request.files["h_img"]
        v_skill = request.form["h_skill"]
        v_story = request.form["h_story"]
        v_imgname=v_img.filename
        # print(v_imgname)
        v_img.save(os.path.join(os.getcwd()+"\\static\\images\\hero\\",v_imgname))
        db=Hero()
        result=db.insert(v_name,os.path.join("/static/images/hero/",v_imgname),v_skill,v_story)
        # print(result)
        if result>0:
            return "T"
        else:
            return "F"

# 英雄查询
@hero_blue.route('/hero_query', methods=["POST", "GET"])
def hero_query():
    if request.method == "GET":
        db = Hero()
        result=db.hero_select()
        # print(result)
        return render_template("hero.html", u_result=result)
#英雄查询详细
@hero_blue.route('/hero_introduce', methods=["POST", "GET"])
def hero_introduce():
    if request.method == "GET":
        id=request.args.get('id')
        # print(id)
        db = Hero()
        result=db.hero_select_one(id)
        print(result)
        return render_template("hero_introduce.html", u_result=result)
        # return  render_template("login.html")
#英雄查询详细
@hero_blue.route('/hero_buy', methods=["POST", "GET"])
def hero_buy():
    if request.method == "GET":
        id=request.args.get('id')
        # print(id)
        db = Hero()
        result=db.hero_select_one(id)
        return render_template("hero_buy.html", u_result=result)