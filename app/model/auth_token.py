from app import db

class AuthToken(db.Model):
    __tablename__ = 'auth_token'
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "<Token : %s>" % self.token