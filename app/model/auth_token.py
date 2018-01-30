from . import db

class AuthToken(db.Model):
    __tablename__ = 'auth_token'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    token = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return "<Token : %s>" % self.token