from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Chat(db.Model):
    __tablename__ = 'chat'

    id = db.Column(db.String, primary_key=True, index=True)
    user_id = db.Column(db.String)
    messages = db.Column(db.JSON) 

    def __repr__(self):
        return f"<Chat(user_id={self.user_id})>"