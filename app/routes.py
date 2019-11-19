from flask import render_template, url_for, request, redirect
from werkzeug.utils import secure_filename
from app import obj

@obj.route('/')
@obj.route('/home')
def home():
    songs = [
        {
            'name':'Highway To Hell',
            'artist':'AC/DC'
        },
        {
            'name': 'Enemy Inside',
            'artist': 'Dream Theatre'
        }    
    ]
    return render_template('home.html', songs=songs)

@obj.route('/upload', methods=['GET','POST'])
def upload():
    return render_template('upload.html')
