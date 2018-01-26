import enum
from datetime import datetime
from app import db
from .user import User

class TodoStatusEnum(enum.Enum):
    not_completed = 'not completed'
    completed = 'completed'
    deleted = 'deleted'

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer)
    todo_id = db.Column(db.String(50), unique=True, index=True)
    todo_task = db.Column(db.Text, nullable=False)
    status = db.Column(db.Enum(TodoStatusEnum), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    user_id = db.Column(db.String(30), db.ForeignKey(User.user_id), nullable=False)
    

    def __repr__(self):
        return "<Todo : %s>" % self.todo_task


