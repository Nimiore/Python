from flask import render_template, url_for, request, redirect, send_from_directory, flash
from werkzeug.utils import secure_filename
from app import obj, db
from app.models import Song
from tinytag import TinyTag
import urllib.request
import os

ALLOWED_EXTENSIONS = {'mp3'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@obj.route('/')
@obj.route('/home')
def home():
    songs = Song.query.all()
    return render_template('home.html', songs=songs)

@obj.route('/upload', methods=['GET','POST'])
def upload():
    if (request.method=='POST'):
        if('file' not in request.files):
            print('No file added in the request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            print('Valid File')
            filename = secure_filename(file.filename)
            filepath = os.path.join(obj.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            tag = TinyTag.get(filepath)
            title = tag.title
            tagArtist = tag.artist
            tagAlbum = tag.album            
            resourceAudioPath = 'http://localhost:5000/uploads/'+filename            
            song = Song(songname=title, artist=tagArtist, album=tagAlbum, filePath=filepath, resourcePath=resourceAudioPath, isUploaded=True)
            db.session.add(song)
            db.session.commit()
            flash('Song Added')
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('upload.html')

@obj.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(obj.config['UPLOAD_FOLDER'],filename)

@obj.route('/delete/<songid>')
def delete(songid):
    if songid:
        song = Song.query.get(songid)
        if song.isUploaded:
            db.session.delete(song)
            db.session.commit()
    return redirect(url_for('home'))

@obj.route('/song/<songid>', methods=['GET','POST'])
def song(songid):
    print('aagaya')
    if songid:
        song = Song.query.get(songid)
        filepath = song.filePath
        tag = TinyTag.get(filepath)
        return render_template('song.html', song=song, tag=tag)

@obj.route('/download/<songid>', methods=['GET','POST'])
def download(songid):
    if (request.method=='POST'):
        song = Song.query.get(songid)
        if song:
            filename = song.songname+'.mp3'            
            filedata = urllib.request.urlopen(song.resourcePath)
            dataToWrite = filedata.read()
            with open(os.path.join(obj.config['DOWNLOAD_FOLDER'], filename),'wb') as f:
                f.write(dataToWrite)
    return redirect(url_for('song', songid=songid))

@obj.route('/search', methods=['GET','POST'])
def search():    
    if request.method=='POST':
        query = request.form.get('search')
        if query:
            return redirect(url_for('searchResults',query=query))
    return redirect(url_for('home'))

@obj.route('/searchResults/<query>', methods=['GET','POST'])
def searchResults(query):
    if query:
        queryStr = '%{0}%'.format(query)    
        results=Song.query.filter((Song.songname.ilike(queryStr))|(Song.artist.ilike(queryStr))|(Song.album.ilike(queryStr)))
        print(results)
        return render_template('searchResults.html',results=results)
    return redirect(url_for('home'))


