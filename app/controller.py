from cmath import log
from flask import Blueprint, render_template, flash, request, redirect, url_for, jsonify

from . import db
from .models import Batch, Category, Course, Enquiry, Qualification, User
import json

controller = Blueprint('controller', __name__)

def get_general_courses():
    rt={}
    instructors= User.query.filter_by(role_id='ins')
    categories =Category.query.all()
    
    rt["filter"]=[]
    cat_items=[]
    for i in categories:
        cat_items.append(i.category_name)
    rt["filter"].append({"name":"category","items":cat_items})
    ins_items=[]
    for i in instructors:
        ins_items.append(i.full_name)
    rt["filter"].append({"name":"instructor","items":ins_items})
    rt["filter"].append({"name":"status","items":["active","disabled"]})


    rt["main"]=[]
    courses =Course.query.all()
    for i in courses:
        # name of the instructor
        rt["main"].append({
            "title":i.course_name,
            "sub_title":User.query.filter_by(user_id = Course.query.filter_by(course_id=i.course_id).first().instructor_id).first().full_name,
            "link": "/user/"+i.course_id
        })
    rt["page"]={
            "number":"1",
            "left":"hidden",
            "right":""
        }
    rt["rows"]="5"
    rt["showing_results"]={
            "results":"5",
            "of":"5"
        }
    rt["url"]="/user/courses"
    return rt
    
