import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '12345'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:////'+os.path.join(basedir,'music.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.environ.get('SECRET_KEY') or os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
    DOWNLOAD_FOLDER = os.path.join(os.path.expanduser('~'), 'Downloads')
