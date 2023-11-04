# java page

import data.db_session as session
from data.users import User
from flask import redirect, render_template
from flask_login import  logout_user, login_required, login_user
import flask
from wtforms import PasswordField, SubmitField, EmailField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from data.users import User

blueprint = flask.Blueprint('java', __name__, template_folder='templates')


dictt = {
    1: ["Data Types", "java/1"],
    2: [ "Comments", "java/2"],
    3: ["Input / Output", "java/3"],
    4: ["Operators", "java/4"],
    5: ["If / else", "java/5"],
    6: ["Switch Statement", "java/6"],
    7: ["While", "java/7"],
    8: ["For", "java/8"],
    9: ["Nested Loop", "java/9"],
    10: ["Break And Continue", "java/10"],
    11: ["Array", "java/11"],
    12: ["Array List", "java/12"],
    13: ["Class And Object", "java/13"],
    14: ["Keyword 'This'", "java/14"],
    15: ["Constructor", "java/15"],
    16: ["Modifiers", "java/16"],
    17: ["Methods", "java/17"]
}


@blueprint.route('/java')
@login_required
def java():
    return render_template('java.html', title='java', data=dictt)


@blueprint.route('/java/<int:number>')
@login_required
def java_pages(number):
    return render_template(f'java_theory/{number}.html', title='java', data=dictt)










@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")