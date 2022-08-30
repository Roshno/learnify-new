from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

basedir = path.abspath(path.dirname(__file__))

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '5c09a9c8222e15531612efe631c23122d9bb5c56'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(basedir, 'database' ,'db.sqlite3')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    print(app.config['SQLALCHEMY_DATABASE_URI'])

    from .views import views
    from .controller import controller

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(controller, url_prefix='/c')

    from .models import User, UserQualification, Role, ActivityLog, Qualification, Category, Course, CourseRequirement, Batch, Enrollment, Enquiry

    create_database(app)

    return app



def create_database(app):
    if not path.exists('app/' + 'DB_NAME'):
        db.create_all(app=app)
        print('Created Database!')