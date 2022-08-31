from flask import Blueprint, render_template, flash, request
from flask_login import login_required, current_user
from . import db
from .models import Batch, Category, Course, Enquiry, Qualification, User

views = Blueprint('views', __name__)

@views.route('/admin')
def home():
    return render_template('base.html', username=current_user.full_name, email=current_user.email)

@views.route('/admin/users', methods=['GET'])
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@views.route('/admin/courses', methods=['GET', 'POST'])
def courses():
    if request.method == 'POST':
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
        new_course = Course(course_id=course_id, course_name=course_name, category_id=category_id, course_duration=course_duration, instructor_id=instructor_id, max_batch_size=max_batch_size, description=description, preview_video=preview_video, syllabus=syllabus, status=status, narration=narration)
        db.session.add(new_course)
        db.session.commit()
    courses = Course.query.all()
    categories = Category.query.all()
    statuses = ["Active", "Disabled"]
    instructors = User.query.join(Course, Course.instructor_id == User.user_id)
    return render_template('courses.html', courses=courses, categories=categories, statuses=statuses, instructors=instructors)

@views.route('/admin/enquiries', methods=['GET'])
def enquiries():
    enquiries = Enquiry.query.all()
    courses = Course.query.all()
    categories = Category.query.all()
    statuses = ["Selected", "Admitted", "Rejected", "Closed"]
    instructors = User.query.join(Course, Course.instructor_id == User.user_id)
    return render_template('enquiries.html', enquiries=enquiries, courses=courses, categories=categories, statuses=statuses, instructors=instructors)

@views.route('/admin/categories', methods=['GET'])
def categories():
    categories = Category.query.all()
    return render_template('categories.html', categories=categories)

@views.route('/admin/qualifications', methods=['GET'])
def qualifications():
    qualifications = Qualification.query.all()
    return render_template('qualifications.html', qualifications=qualifications)

@views.route('/admin/batches', methods=['GET'])
def batches():
    batches = Batch.query.all()
    return render_template('batches.html', batches=batches)