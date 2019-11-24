# Python
A Flask/Python project for Music aaplication

This application is a music management/streaming platform where a user could upload/download/play/delete/search songs.
It uses Flask-SqlAlchemy and SQLite database.

Prerequisites:
    This application is implemented using python3 version. So you would need to install it.

Assumptions and Implementation Guide:
    The application only supports .mp3 files as of now.
    All songs go in a common playlist which is generated at your 'home' page.
    For retrieving the metadata(title/album/artist) for songs, I am using 'TinyTag' package.
    The 'Song' model is designed to have a boolean value - 'isUploaded'. So that the user would be able to delete only those songs which are uploaded by the user.
    The database should have atleast one entry, so the 1st record should not be deleted. (Design-Flaw : Fixing it to be considered for future enhancement)

Future Enhancement for identified potential Security Vulnerabilities:
    Encrypting ids passed inside the html-tags.
    More secure searching mechanism.
    

   



