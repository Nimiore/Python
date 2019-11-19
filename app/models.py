from app import db

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    songname = db.Column(db.String(150), index=True)
    artist = db.Column(db.String(150), index=True)
    album = db.Column(db.String(150), index=True)
