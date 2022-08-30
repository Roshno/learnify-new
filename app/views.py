from flask import Blueprint, render_template, flash, request

from . import db
from .models import Batch, Category, Course, Enquiry, Qualification, User

views = Blueprint('views', __name__)


@views.route('/admin/users', methods=['GET'])
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@views.route('/admin/courses', methods=['GET'])
def courses():
    courses = Course.query.all()
    categories = Category.query.all()
    statuses = ["Active", "Disabled"]
    instructors = User.query.join(Course, Course.instructor_id == User.user_id)
    return render_template('courses.html', courses=courses, categories=categories, statuses=statuses, instructors=instructors)

@views.route('/admin/enquiries', methods=['GET'])
def enquiries():
    enquiries = Enquiry.query.all()
    return render_template('enquiries.html', enquiries=enquiries)

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