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


# fields of the log in page
class LoginForm(FlaskForm):

    email = EmailField('Email', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Log in')

# fields of the sign up page
class RegistrationForm(FlaskForm):

    email = EmailField('Email', validators=[DataRequired()])

    name = StringField('Name', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Sign up')


# log in page
@blueprint.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    db_session = session.create_session() # connecting to database

    if form.validate_on_submit(): # if all fields are completed 

        user = db_session.query(User).filter(User.email == form.email.data).first() # getting user with this email from database

        if user is not None: # if there is such user in database ( he need to sign up first )
            pas = user.password

            if user and user.check_password(pas, form.password.data): # checking if passwords match

                login_user(user) # remembering user

                return redirect(f'/homepage') # redirecting user to the next page

            return render_template('login.html', message='Wrong email or password', form=form) # forcing user to complete form again
        
        return render_template('login.html', message='Wrong email or password', form=form)  # forcing user to complete form again

    return render_template('login.html', title='T-help | Login', form=form)  # forcing user to complete form again


# sign up page
@blueprint.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm() 
    db_session = session.create_session() # connecting to the database

    if form.validate_on_submit(): # if all fields are completed 

        if db_session.query(User).filter(User.email == form.email.data).first(): # if there is this email arleadu in databse

            return render_template('signup.html', title='Registration', form=form, message="The current email is already used")
       
       # adding user's data
        user = User(
            email=form.email.data,
            leetcode_name=form.name.data,
        )
        
        # setting password
        user.set_password(form.password.data)
        user.password = user.password_hash

        # adding user to the database
        db_session.add(user)
        db_session.commit()

        login_user(user) # remembering user

        return redirect(f'/homepage') # redirecting user to the next page

    return render_template('signup.html', title='T-help | Registration', form=form) # forcing user to complete form again


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")
