# home page

import data.db_session as session
from data.users import User
from flask import redirect, render_template
from flask_login import  logout_user, login_required, login_user
import flask
from wtforms import PasswordField, SubmitField, EmailField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from data.users import User

blueprint = flask.Blueprint('homepage', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET', 'POST'])
@blueprint.route('/homepage')
@login_required
def homepage():
    return render_template('homepage.html', title='homepage', img=['java_logo.jpeg', 'python_logo.png'])


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")
