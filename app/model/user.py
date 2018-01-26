from datetime import datetime
from . import db
from .todo import Todo

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(30), unique=True, index=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    create_at = db.Column(db.DateTime(), default=datetime.now())
    updated_at = db.Column(db.DateTime(), onupdate=datetime.now())
    todos = db.relationship(Todo, backref='user', lazy=True)


    def __repr__(self):
        return "<User : %s>" % self.username
    