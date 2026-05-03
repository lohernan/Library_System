from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    available = db.Column(db.Boolean, default=True)

class Borrower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    borrower_id = db.Column(db.Integer, db.ForeignKey('borrower.id'))
    due_date = db.Column(db.DateTime, default=lambda: datetime.now() + timedelta(days=14))