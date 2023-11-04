from data import db_session
from flask import Flask
from flask_login import LoginManager
import datetime

from CODE.data.users import User

from CODE.pages import log_reg, homepage, javapage,pythonpage



app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=1)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


if __name__ == '__main__':

    db_session.global_init("CODE/db/data.db")


    # register web pages

    app.register_blueprint(log_reg.blueprint)
    app.register_blueprint(homepage.blueprint)
    app.register_blueprint(javapage.blueprint)
    app.register_blueprint(pythonpage.blueprint)


    app.run()