from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///support_tickets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()


class SupportTicket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    ticket_status = db.Column(db.String(25), default = "New", nullable=False)
    ticket_title = db.Column(db.String(50), nullable=False)
    ticket_description = db.Column(db.String(300), nullable=True)
    date_updated = db.Column(db.DateTime)
    update_note = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return '<Record %r>' %self.id

class LoginCredentials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cred_user = db.Column(db.String(50), nullable=False)
    cred_password = db.Column(db.String(50), nullable=False)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    positionTitle = db.Column(db.String(50), nullable=False)
    positionSpeciality = db.Column(db.String(50), nullable=False)