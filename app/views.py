from cmath import log
from flask import Blueprint, render_template, flash, request, redirect, url_for, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Batch, Category, Course, Enquiry, Qualification, User
import json
from . import controller
views = Blueprint('views', __name__)


@views.route('/admin')
@login_required
def home():
    return render_template('base.html', username=current_user.full_name, email=current_user.email)


@views.route('/admin/users', methods=['GET'])
@login_required
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@views.route('/admin/courses/<courseId>', methods=['DELETE'])
def deleteCourse(courseId):
    course = Course.query.get(courseId)
    if course:
        db.session.delete(course)
        db.session.commit()
    return jsonify({})

@views.route('/admin/courses', methods=['GET', 'POST'])
@login_required
def courses():
    if request.method == 'POST':
        req_type = request.form.get('type')
        course_id = request.form.get('add_course_id')
        course_name = request.form.get('add_course_name')
        category_id = request.form.get('add_course_category')
        course_duration = request.form.get('add_course_duration')
        max_batch_size = request.form.get('add_max_batch_size')
        instructor_id = request.form.get('add_course_instructor')
        description = request.form.get('add_course_description')
        preview_video = request.form.get('add_preview_video')
        status = request.form.get('add_status')
        syllabus = request.form.get('add_course_syllabus')
        narration = request.form.get('add_course_narration')

        if req_type == 'update':
            course = Course.query.get(course_id)
            if course:
                db.session.delete(course)
                db.session.commit()

        new_course = Course(course_id=course_id, course_name=course_name, category_id=category_id, course_duration=course_duration, instructor_id=instructor_id, max_batch_size=max_batch_size, description=description, preview_video=preview_video, syllabus=syllabus, status=status, narration=narration)
        db.session.add(new_course)
        db.session.commit()

    courses = Course.query.all()
    categories = Category.query.all()
    statuses = ["Active", "Disabled"]
    instructors = User.query.join(Course, Course.instructor_id == User.user_id)
    return render_template('courses.html', courses=courses, categories=categories, statuses=statuses, instructors=instructors)

@views.route('/admin/enquiries', methods=['GET'])
@login_required
def enquiries():
    
    enquiries = Enquiry.query.all()
    courses = Course.query.all()
    categories = Category.query.all()
    statuses = ["Selected", "Admitted", "Rejected", "Closed"]
    instructors = User.query.join(Course, Course.instructor_id == User.user_id)
    return render_template('enquiries.html', enquiries=enquiries, courses=courses, categories=categories, statuses=statuses, instructors=instructors)

@views.route('/admin/categories', methods=['GET'])
@login_required
def categories():
    categories = Category.query.all()
    statuses =["active","disabled"]
    return render_template('categories.html', categories=categories,statuses=statuses )

@views.route('/admin/qualifications', methods=['GET'])
@login_required
def qualifications():
    qualifications = Qualification.query.all()
    statuses =["active","disabled"]
    return render_template('qualifications.html', qualifications=qualifications,statuses=statuses)

@views.route('/admin/batches', methods=['GET', 'POST'])
@login_required
def batches():
    if request.method == "POST":
        req_type = request.form.get('type')
        batch_id = request.form.get('batch_id')
        batch_name = request.form.get('batch_name')
        course_id = request.form.get('course_id')
        status = request.form.get('status')

        if req_type == 'update':
            batch = Batch.query.get(batch_id)
            if batch:
                db.session.delete(batch)
                db.session.commit()

        new_batch = Batch(course_id=course_id, batch_id=batch_id, batch_name=batch_name, status=status)
        db.session.add(new_batch)
        db.session.commit()

    batches = Batch.query.all()
    courses = Course.query.all()
    statuses =["active","disabled"]
    return render_template('batches.html', batches=batches, statuses =statuses,courses=courses)

@views.route('/user/profile',methods=["GET","POST"])
def user_profile():
    data = {"name":"Joel","email":"joel@gmail.com","phone":"9388775","role":"trainee","qualification_list":["btech","mtech","mcom"],"user_qualifications":["btech"]}
    if request.method == "GET":
        return render_template('user_profile.html',data=data)
    elif request.method =="POST":
        print(request.json)
        return ""

@views.route('/user/courses', methods=['GET'])
def user_general_courses():
    print(len(request.args))
    # data ={
    #     "filter":[
    #         {
    #             "name": "category",
    #             "items": [
    #                 "all", "coding", "buisness","arts","engineering"
    #             ]
    #         },
    #         {
    #             "name": "status",
    #             "items": [
    #                 "all", "active","disabled"
    #             ]
    #         },
    #         {
    #             "name": "instructor",
    #             "items": [
    #                 "all","Big Josher","Simon Minter"
    #             ]
            
    #         }
    #     ],
    #     "main":[
    #         {
    #             "title":"title-1",
    #             "sub_title":"subtitle-1",
    #             "link":"/user/c1"
    #         },
    #         {
    #             "title":"title-2",
    #             "sub_title":"subtitle-2",
    #             "link":"/user/2"
    #         },
    #         {
    #             "title":"title-3",
    #             "sub_title":"subtitle-3",
    #             "link":"/user/3"
    #         },
    #         {
    #             "title":"title-4",
    #             "sub_title":"subtitle-4",
    #             "link":"/user/4"
    #         },
    #         {
    #             "title":"title-5",
    #             "sub_title":"subtitle-5",
    #             "link":"/user/5"
    #         }
    #     ],
    #     "page":{
    #         "number":"1",
    #         "left":"hidden",
    #         "right":""
    #     },
    #     "rows":"5",
    #     "showing_results":{
    #         "results":"5",
    #         "of":"5"
    #     },
    #     "url":"/user/courses"
    # }
    data = controller.get_general_courses()
    print(request.args)
    return render_template('user_general_courses.html',data=data)
    



# @views.route('/user/<string:course_id>/enquire',methods=["POST"])
# def user_enquire():
#     pass

@views.route('/user/mycourses',methods=["GET"])
def user_mycourses():
    data ={
        "filter":[
            {
                "name": "category",
                "items": [
                    "all", "coding", "buisness","arts","engineering"
                ]
            },
            {
                "name": "status",
                "items": [
                    "all", "active","disabled"
                ]
            },
            {
                "name": "instructor",
                "items": [
                    "all","Big Josher","Simon Minter"
                ]
            
            }
        ],
        "main":[
            {
                "title":"title-1",
                "sub_title":"subtitle-1",
                "link":"http://127.0.0.1:5000/user/1"
            },
            {
                "title":"title-2",
                "sub_title":"subtitle-2",
                "link":"http://127.0.0.1:5000/user/2"
            },
            {
                "title":"title-3",
                "sub_title":"subtitle-3",
                "link":"http://127.0.0.1:5000/user/3"
            },
            {
                "title":"title-4",
                "sub_title":"subtitle-4",
                "link":"http://127.0.0.1:5000/user/4"
            },
            
        ],
        "page":{
            "number":"1",
            "left":"hidden",
            "right":"hidden"
        },
        "rows":"5",
        "showing_results":{
            "results":"5",
            "of":"5"
        },
        "url":"http://127.0.0.1:5000/user/mycourses"
    }
    return render_template('user_mycourses.html',data=data)

@views.route('/user/myenquiries',methods=["GET"])
def user_myenquiries():
    data ={
        "filter":[
            {
                "name": "courses",
                "items": [
                    "cpp", "java", "python","angular","oilpainting"
                ]
            },
            {
                "name": "status",
                "items": [
                    "all", "active","disabled"
                ]
            },
            {
                "name": "instructor",
                "items": [
                    "all","Big Josher","Simon Minter"
                ]
            
            }
        ],
        "main":[
            {
                "title":"title-1",
                "sub_title":"subtitle-1",
                "link":"/user/e1"
            },
            {
                "title":"title-2",
                "sub_title":"subtitle-2",
                "link":"/user/e2"
            },
            {
                "title":"title-3",
                "sub_title":"subtitle-3",
                "link":"/user/e3"
            },
            {
                "title":"title-4",
                "sub_title":"subtitle-4",
                "link":"/user/e4"
            },
            {
                "title":"title-5",
                "sub_title":"subtitle-5",
                "link":"/user/e5"
            }
        ],
        "page":{
            "number":"1",
            "left":"hidden",
            "right":""
        },
        "rows":"5",
        "showing_results":{
            "results":"5",
            "of":"5"
        },
        "url":"/user/myenquiries"
    }
    print(request.args)
    return render_template('user_myenquiries.html',data=data)

@views.route('/user/enquiry/<string:enquiry>',methods=["GET","PUT"])
def user_enquiry():
    pass
@views.route('/user/<id>',methods=["GET","POST"])
def user(id):
    print(id)
    if request.method == 'GET':
        data = {"course_id":2,"course_name":"coding on cpp","course_duration":4,"instructor":"Big Josher","max_batch_size":20,"description":"description","preview_video":"https://www.youtube.com/embed/tgbNymZ7vqY"}
        return render_template('course_detail.html',data=data)
    else:
        print(request.json['course_id'])
        return ""
# @views.route('/db')
# def db():
#     controller.get_general_courses()
#     return ""



