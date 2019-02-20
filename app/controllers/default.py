import os

from app import app
from app import db
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    def __repr__(self):
        return "<Title: {}>".format(self.title)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        book = Book(title=request.form.get("title"))   
        db.session.add(book)
        db.session.commit()
    books = Book.query.all()
    return render_template("home.html",books=books)