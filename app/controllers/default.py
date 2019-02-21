import os

from app import app
from app import db
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from app.models.tables import Book

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        book = Book(
            title=request.form.get("title"),
            number_of_pages = request.form.get("numberpages"),
            rate = request.form.get("rate")
        )   
        db.session.add(book)
        db.session.commit()
    books = Book.query.all()
    return render_template("home.html",books=books)