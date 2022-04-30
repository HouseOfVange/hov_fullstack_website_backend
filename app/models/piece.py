from sqlalchemy.orm import backref
from app import db

class Piece(db.Model):
    piece_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String)
    client = db.Column(db.String)
    like_count = db.Column(db.Integer)