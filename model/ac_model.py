from flask import Flask,render_template,request,Blueprint
from database.db_activity import  Activity
ac_blue=Blueprint("ac_model",__name__)
import os
#活动发布
@ac_blue.route("/activity_manager_pro",methods=["POST","GET"])
def activity_manager_pro():
    if request.method=="POST":
        v_name=request.form["a_name"]
        v_time = request.form["a_time"]
        v_content = request.form["a_content"]
        v_img=request.files["a_img"]
        v_bimg=request.files["ab_img"]
        v_imgname=v_img.filename
        v_bimgnmae=v_bimg.filename
        # 路径拼接
        v_img.save(os.path.join(os.getcwd()+"\\static\\images\\activity\\small\\",v_imgname))
        v_img.save(os.path.join(os.getcwd()+"\\static\\images\\activity\\big\\",v_bimgnmae))
        db=Activity()
        result=db.insert(v_name,v_time,os.path.join("/static/images/activity/small/",v_imgname),v_content,os.path.join("/static/images/activity/big/",v_bimgnmae))
        print(result)
        if result>0:
            return "T"
        else:
            return "F"
        # print(v_name,v_time,v_content)

# 活动查询
@ac_blue.route('/activity_query', methods=["POST", "GET"])
def activity_query():
    if request.method == "GET":
        db = Activity()
        result=db.ac_select()
        print(result)
        return render_template("activity.html", u_result=result)

# 活动详细查询
@ac_blue.route('/activity_query_one', methods=["POST", "GET"])
def activity_query_one():
    if request.method == "GET":
        id = request.args.get('id')
        db = Activity()
        result = db.ac_select_one(id)
        return render_template("activity_introduce.html", u_result=result)