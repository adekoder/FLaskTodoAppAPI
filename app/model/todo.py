import enum
from datetime import datetime
from . import db

class TodoStatusEnum(enum.Enum):
    not_completed = 'not completed'
    completed = 'completed'
    deleted = 'deleted'

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    todo_id = db.Column(db.String(50), unique=True, index=True)
    todo_task = db.Column(db.Text, nullable=False)
    status = db.Column(db.Enum(TodoStatusEnum), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    user_id = db.Column(db.String(30), db.ForeignKey('users.user_id'), nullable=False)
    
    def __repr__(self):
        return "<Todo : %s>" % self.todo_task

    def save(self):
        db.session.add(self)
        db.session.commit()
