from flask import Blueprint, render_template, flash, request

from . import db
from .models import Category, Course, User

controller = Blueprint('controller', __name__)


