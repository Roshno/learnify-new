from flask import Blueprint, render_template, flash, request

from . import db


controller = Blueprint('controller', __name__)


@controller.route('/', methods=['GET'])
def home():
    return "Hi controller"