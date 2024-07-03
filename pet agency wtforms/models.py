from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(30), nullable=False)
    photo_url = db.Column(db.String(200), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)