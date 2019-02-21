import os

from app import app
from app import db
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from app.models.tables import Book

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/listbooks")
def listbooks():
    books = Book.query.all()
    app.jinja_env.filters['page_title'] = "listbooks"
    return render_template("listbooks.html",books=books)

@app.route("/cadbook",methods=["GET", "POST"])
def cadbook():
    if request.form:
        book = Book(
            title=request.form.get("title"),
            number_of_pages = request.form.get("numberpages"),
            rate = request.form.get("rate")
        )   
        db.session.add(book)
        db.session.commit()
    return render_template("cadbook.html")