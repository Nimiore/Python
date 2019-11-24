from app import db

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    songname = db.Column(db.String(150), index=True)
    artist = db.Column(db.String(150), index=True)
    album = db.Column(db.String(150), index=True)
    filePath = db.Column(db.String(250), index=True)
    resourcePath = db.Column(db.String(250), index=True)
    isUploaded = db.Column(db.Boolean, default=False, nullable=False)

def __repr__(self):
   return f"<id={self.id}, songname={self.songname}>"
