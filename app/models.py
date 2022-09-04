from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin

class Init():
    pass

class UserQualification(db.Model):
    usr_q_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    qualification_id = db.Column(db.String(25), db.ForeignKey("qualification.qualification_id"))


class Role(db.Model):
    role_id = db.Column(db.String(25),primary_key =True)
    role_name = db.Column(db.String(25))

    role_members = db.relationship('User')

class Qualification(db.Model):
    qualification_id = db.Column(db.String(25),primary_key =True)
    qualification_name = db.Column(db.String(25))
    status = db.Column(db.String(25))

   # qualified_members = db.relationship('UserQualification')

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer,primary_key =True)
    full_name = db.Column(db.String(25))
    hashed_password = db.Column(db.String(25))
    role_id = db.Column(db.String(25),db.ForeignKey('role.role_id'))
    email = db.Column(db.String(25))
    phone = db.Column(db.String(25))
    
    activity_log = db.relationship('ActivityLog')
    enrolled_courses = db.relationship('Enrollment')
    enquiries = db.relationship('Enquiry')
    qualifications = db.relationship('UserQualification')

    def get_id(self):
        return (self.user_id)


class ActivityLog(db.Model):
    log_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    timestamp = db.Column(db.DateTime(timezone=True), default=func.now())






class Category(db.Model):
    category_id = db.Column(db.String(25),primary_key =True)
    category_name = db.Column(db.String(25))
    status = db.Column(db.String(25))
    narration = db.Column(db.String(25))
    
    mapped_courses = db.relationship('Course')


class Course(db.Model):
    course_id = db.Column(db.String(25),primary_key=True)
    course_name = db.Column(db.String(25))
    category_id = db.Column(db.String(25),db.ForeignKey('category.category_id'))
    course_duration = db.Column(db.Integer)
    instructor_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    max_batch_size = db.Column(db.String(25))
    description = db.Column(db.String(50))
    preview_video = db.Column(db.String(50))
    syllabus = db.Column(db.String(100))
    rating = db.Column(db.String(25))
    status = db.Column(db.String(25))
    narration = db.Column(db.String(25))
    
    course_enrolled_trainees = db.relationship('Enrollment')
    enquiries = db.relationship('Enquiry')
    batches = db.relationship('Batch')
    course_qualification_reqirements = db.relationship('CourseRequirement')


class CourseRequirement(db.Model):
    requirement_id = db.Column(db.String(25),primary_key =True)
    course_id = db.Column(db.String(25),db.ForeignKey('course.course_id'))
    qualification_id = db.Column(db.Integer,db.ForeignKey('qualification.qualification_id'))
    min_percentage = db.Column(db.String(25))


class Batch(db.Model):
    batch_id = db.Column(db.String(25),primary_key =True)
    batch_name = db.Column(db.String(25))
    course_id = db.Column(db.String(25),db.ForeignKey('course.course_id'))
    status = db.Column(db.String(25))
    
    batch_enrolled_trainees = db.relationship('Enrollment')


class Enrollment(db.Model):
    enrollment_id = db.Column(db.Integer,primary_key =True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    course_id = db.Column(db.String(25),db.ForeignKey('course.course_id'))
    batch_id = db.Column(db.String(25),db.ForeignKey('batch.batch_id'))
    status = db.Column(db.String(25))
    score = db.Column(db.String(25))


class Enquiry(db.Model):
    enquiry_id = db.Column(db.String(25),primary_key =True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    course_id = db.Column(db.String(25),db.ForeignKey('course.course_id'))
    enquiry = db.Column(db.String(100))
    status = db.Column(db.String(25))
    comment = db.Column(db.String(50))