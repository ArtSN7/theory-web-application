import sqlalchemy
from flask_login import UserMixin
from .db_session import SqlAlchemyBase
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy_serializer import SerializerMixin


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    email = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    password = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    leetcode_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, pas, password):
        return check_password_hash(pas, password)


    def __repr__(self):
        return '<User{}>'.format(self.leetcode_name)