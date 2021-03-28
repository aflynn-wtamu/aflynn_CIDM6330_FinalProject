from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from app_db import app, BookDB, db

@app.route('/')
def index():
    return render_template('index.html')

# Add Action
@app.route('/add', methods=['GET','POST'])
def create():
    if request.method=='POST':
        bookmark_title = request.form['title']
        bookmark_url = request.form['url']
        bookmark_notes = request.form['notes']
        new_bookmark = BookDB(book_title=bookmark_title,book_url=bookmark_url,book_notes=bookmark_notes)
        try:
            db.session.add(new_bookmark)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error adding the bookmark'
    else:
        return render_template('methods/add.html')


# List by date action
@app.route('/listdate')
def listdate():
    #return 'Count: ' + str(BookDB.query.count())
    bookmarks = BookDB.query.order_by(BookDB.date_added).all()
    return render_template('methods/listdate.html', bookmarks=bookmarks)


# List by title action
@app.route('/listtitle')
def listtitle():
    bookmarks = BookDB.query.order_by(BookDB.book_title).all()
    return render_template('methods/listtitle.html', bookmarks=bookmarks)


# Delete action
@app.route('/delete/<int:id>')
def delete(id):
    bookmark_to_delete = BookDB.query.get_or_404(id)

    try:
        db.session.delete(bookmark_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an error deleting the bookmark'

if __name__ == "__main__":
    app.run(debug=True)
