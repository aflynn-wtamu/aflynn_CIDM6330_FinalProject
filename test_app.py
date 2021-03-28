import unittest
from app import app
from app_db import BookDB, db
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

LOCALHOST = 'http://127.0.0.1:5000/'

class AppTestCase(unittest.TestCase):
    
    def test_add(self):
        tester = app.test_client(self)
        response = tester.get("/add")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

        test_title = '1984'
        test_url = 'www.1984.biz'
        test_notes = 'war is peace'
        new_bookmark = BookDB(book_title=test_title,book_url=test_url,book_notes=test_notes)
        try:
            db.session.add(new_bookmark)
            db.session.commit()
            pass
        except:
            return 'There was an error adding the bookmark'
    
    def test_delete(self):
        record_id = BookDB.query.order_by(BookDB.id.desc()).first().id
        #tester = app.test_client(self)
        #response = tester.get(f'/delete/{record_id}')
        #statuscode = response.status_code
        #self.assertEqual(statuscode, 302)
        
        bookmark_to_delete = BookDB.query.get_or_404(record_id)
        try:
            db.session.delete(bookmark_to_delete)
            db.session.commit()
            pass
        except:
            return 'There was an error deleting the bookmark'