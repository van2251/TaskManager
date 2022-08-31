from app import db
from datetime import datetime

class Task(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    date=db.Column(db.Date,nullable=False)

    def _repr_(self):
        return f'{self.title}'