from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):
    """ pet list for adoption"""

    __tablename__ = "pet_list"

    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species= db.Column(db.Text, nullable=False)
    photo_url=db.Column(db.Text, nullable=True)
    age=db.Column(db.Integer, nullable=True)
    notes=db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)

def connect_db(app):
    db.app = app
    db.init_app(app)
