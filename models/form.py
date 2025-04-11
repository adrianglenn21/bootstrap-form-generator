from settings import db
from sqlalchemy.ext.mutable import MutableDict

class Form(db.Model):
    __tablename__ = "tbl_form"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    questions = db.Column(MutableDict.as_mutable(db.JSON))
    
    def __init__(self):
        self.questions = {"questions": []}