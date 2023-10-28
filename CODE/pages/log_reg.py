# Log In and Sign Up pages

import data.db_session as session
from data.users import User
from flask import redirect, render_template
from flask_login import  logout_user, login_required, login_user
import flask
from wtforms import PasswordField, SubmitField, EmailField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from data.users import User

blueprint = flask.Blueprint('log_reg', __name__, template_folder='templates')



class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Log in')


class RegistrationForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])

    name = StringField('Name', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Sign up')


@blueprint.route('/', methods=['GET', 'POST'])
@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    db_session = session.create_session()

    if form.validate_on_submit():

        user = db_session.query(User).filter(User.email == form.email.data).first()

        if user is not None:
            pas = user.password

            if user and user.check_password(pas, form.password.data):
                login_user(user)

                return redirect(f'/homepage')

            return render_template('login.html', message='Wrong email or password', form=form)
        
        return render_template('login.html', message='Wrong email or password', form=form)

    return render_template('login.html', title='T-help | Login', form=form)


@blueprint.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    db_session = session.create_session()

    if form.validate_on_submit():

        if db_session.query(User).filter(User.email == form.email.data).first():
            return render_template('signup.html', title='Registration', form=form,
                                   message="The current email is already used")

        user = User(
            email=form.email.data,
            leetcode_name=form.name.data,
        )

        user.set_password(form.password.data)
        user.password = user.password_hash

        db_session.add(user)
        db_session.commit()

        login_user(user)

        return redirect(f'/homepage') 

    return render_template('signup.html', title='T-help | Registration', form=form)


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")
